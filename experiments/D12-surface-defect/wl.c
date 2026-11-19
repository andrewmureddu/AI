/*
 * wl.c -- Wang-Landau density of states for the q-state Potts model on a
 * periodic hypercubic lattice (d = 2 or 3), restricted to an energy window.
 *
 * Energy index k = number of satisfied bonds (H = -J * k, J = 1).
 * The walker is confined to k in [kmin, kmax]; moves leaving the window are
 * rejected (and the current bin is updated, as usual for windowed WL).
 *
 * Schedule: Belardinelli-Pereyra.  Initial phase halves ln f each time every
 * reachable bin in the window (all of them for q >= 3, the even-parity ones for
 * q = 2) has been visited since the last halving (checked every
 * 10*nbin trials), until ln f < 1/t; then the 1/t algorithm of Belardinelli & Pereyra (2007),
 * t = trials / (number of visited bins), until ln f < lnf_final.
 * Bins never visited are reported with ln g = NaN and excluded from the
 * flatness check (this handles parity-forbidden levels, e.g. q = 2).
 *
 * Usage: wl q d L kmin kmax seed lnf_final out.txt
 * Output: lines "k ln_g visited_flag"
 * Deterministic given seed (xoshiro256**).
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <string.h>

static uint64_t s[4];
static inline uint64_t rotl(const uint64_t x, int k) { return (x << k) | (x >> (64 - k)); }
static inline uint64_t next(void) {
    const uint64_t r = rotl(s[1] * 5, 7) * 9, t = s[1] << 17;
    s[2] ^= s[0]; s[3] ^= s[1]; s[1] ^= s[2]; s[0] ^= s[3]; s[2] ^= t; s[3] = rotl(s[3], 45);
    return r;
}
static inline double unif(void) { return (next() >> 11) * 0x1.0p-53; }
static inline uint32_t randint(uint32_t n) { return (uint32_t)(((next() >> 32) * (uint64_t)n) >> 32); }
static void seed_rng(uint64_t seed) {
    for (int i = 0; i < 4; i++) {           /* splitmix64 */
        uint64_t z = (seed += 0x9e3779b97f4a7c15ULL);
        z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL;
        z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL;
        s[i] = z ^ (z >> 31);
    }
}

int main(int argc, char **argv) {
    if (argc != 9) { fprintf(stderr, "usage: wl q d L kmin kmax seed lnf_final out\n"); return 1; }
    int q = atoi(argv[1]), d = atoi(argv[2]), L = atoi(argv[3]);
    int kmin = atoi(argv[4]), kmax = atoi(argv[5]);
    uint64_t seed = strtoull(argv[6], 0, 10);
    double lnf_final = atof(argv[7]);
    const char *out = argv[8];
    seed_rng(seed);

    int N = 1; for (int i = 0; i < d; i++) N *= L;
    int z = 2 * d;
    int *nb = malloc(sizeof(int) * N * z);
    for (int i = 0; i < N; i++) {
        int c[3] = {0, 0, 0}, r = i;
        for (int a = 0; a < d; a++) { c[a] = r % L; r /= L; }
        for (int a = 0; a < d; a++) for (int sgn = 0; sgn < 2; sgn++) {
            int cc[3] = {c[0], c[1], c[2]};
            cc[a] = (cc[a] + (sgn ? 1 : L - 1)) % L;
            int j = 0, m = 1;
            for (int b = 0; b < d; b++) { j += cc[b] * m; m *= L; }
            nb[i * z + 2 * a + sgn] = j;
        }
    }
    unsigned char *sp = malloc(N);
    for (int i = 0; i < N; i++) sp[i] = (unsigned char)randint(q);
    long k = 0;
    for (int i = 0; i < N; i++) for (int a = 0; a < z; a += 2) k += (sp[i] == sp[nb[i * z + a]]);

    /* drive into the window greedily */
    long guard = 0;
    while (k < kmin || k > kmax) {
        int i = randint(N), nw = randint(q - 1); if (nw >= sp[i]) nw++;
        int dk = 0; for (int a = 0; a < z; a++) { int c = sp[nb[i * z + a]]; dk += (c == nw) - (c == sp[i]); }
        long k2 = k + dk;
        long dist = k < kmin ? kmin - k : k - kmax, dist2 = k2 < kmin ? kmin - k2 : (k2 > kmax ? k2 - kmax : 0);
        if (dist2 <= dist) { sp[i] = nw; k = k2; }
        if (++guard > 4000000000L) { fprintf(stderr, "could not enter window\n"); return 2; }
    }

    int nbin = kmax - kmin + 1;
    /* reachable levels, by m = dN - k unsatisfied bonds.  q = 2: every
       single-spin flip changes m by an even amount, so m is even, and m = 2 is
       impossible (one flip costs 2d).  q >= 3 in d = 2: m = 1, 2, 3, 5 are
       impossible (one flip 4; a flipped pair 6 or 7).  Checked against exact
       enumeration.  d = 3 is not enumerated here: the caller keeps
       kmax <= 3N - 14, where every level is reachable. */
    int nexp = 0;
    for (int kk = kmin; kk <= kmax; kk++) {
        long m = (long)d * N - kk;
        int ok;
        if (q == 2) ok = (m % 2 == 0) && m != 2;
        else if (d == 2) ok = !(m == 1 || m == 2 || m == 3 || m == 5);
        else ok = m >= 14 || m == 0;
        nexp += ok;
    }
    double *g = calloc(nbin, sizeof(double));
    long *H = calloc(nbin, sizeof(long));
    unsigned char *vis = calloc(nbin, 1);
    double lnf = 1.0;
    int one_over_t = 0;
    long double trials = 0;
    long check = (long)nbin * 10;
    int progress = getenv("WL_PROGRESS") != NULL;
    long it = 0;
    for (;;) {
        int i = randint(N), nw = randint(q - 1); if (nw >= sp[i]) nw++;
        int dk = 0; for (int a = 0; a < z; a++) { int c = sp[nb[i * z + a]]; dk += (c == nw) - (c == sp[i]); }
        long k2 = k + dk;
        if (k2 >= kmin && k2 <= kmax) {
            double dg = g[k - kmin] - g[k2 - kmin];
            if (dg >= 0 || unif() < exp(dg)) { sp[i] = nw; k = k2; }
        }
        int b = (int)(k - kmin);
        g[b] += lnf; H[b]++; vis[b] = 1;
        trials += 1;
        if (one_over_t) {
            if ((++it & 0xFFFF) == 0) {
                int nv = 0; for (int j = 0; j < nbin; j++) nv += vis[j];
                lnf = (double)nv / (double)trials;
                if (lnf < lnf_final) break;
            }
        } else if (++it % check == 0) {
            if (trials > 4e11L) {       /* a wrong reachable-level set must fail loudly, not hang */
                int nv = 0; for (int j = 0; j < nbin; j++) nv += vis[j];
                fprintf(stderr, "abort: initial phase did not finish (visited %d of %d expected)\n", nv, nexp);
                return 3;
            }
            int nv = 0; long hmin = -1;
            for (int j = 0; j < nbin; j++) if (vis[j]) { nv++; if (hmin < 0 || H[j] < hmin) hmin = H[j]; }
            /* Belardinelli-Pereyra initial phase: halve once every visited bin has H > 0 */
            if (hmin > 0 && nv == nexp) {
                if (progress) fprintf(stderr, "lnf=%.3e trials=%.3Le nv=%d\n", lnf, trials, nv);
                lnf *= 0.5;
                memset(H, 0, sizeof(long) * nbin);
                if (lnf < (double)nv / (double)trials) { one_over_t = 1; lnf = (double)nv / (double)trials; }
            }
        }
    }
    FILE *fo = fopen(out, "w");
    fprintf(fo, "# q=%d d=%d L=%d N=%d kmin=%d kmax=%d seed=%llu lnf_final=%g trials=%.6Le\n",
            q, d, L, N, kmin, kmax, (unsigned long long)seed, lnf_final, trials);
    for (int j = 0; j < nbin; j++) fprintf(fo, "%d %.10f %d\n", kmin + j, vis[j] ? g[j] : NAN, vis[j]);
    fclose(fo);
    return 0;
}
