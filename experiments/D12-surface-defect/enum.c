/* enum.c -- exact density of states by full enumeration (validation only).
 * usage: enum q d L out ; prints "k ln_count" for k = satisfied bonds. */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(int argc, char **argv) {
    int q = atoi(argv[1]), d = atoi(argv[2]), L = atoi(argv[3]);
    int N = 1; for (int i = 0; i < d; i++) N *= L;
    int z = 2 * d, nb[64][3];
    for (int i = 0; i < N; i++) {
        int c[3] = {0, 0, 0}, r = i; for (int a = 0; a < d; a++) { c[a] = r % L; r /= L; }
        for (int a = 0; a < d; a++) { int cc[3] = {c[0], c[1], c[2]}; cc[a] = (cc[a] + 1) % L;
            int j = 0, m = 1; for (int b = 0; b < d; b++) { j += cc[b] * m; m *= L; } nb[i][a] = j; }
    }
    int nbond = d * N; double *cnt = calloc(nbond + 1, sizeof(double));
    int sp[64] = {0};
    for (;;) {
        int k = 0; for (int i = 0; i < N; i++) for (int a = 0; a < d; a++) k += sp[i] == sp[nb[i][a]];
        cnt[k] += 1;
        int i = 0; while (i < N && ++sp[i] == q) sp[i++] = 0;
        if (i == N) break;
    }
    FILE *fo = fopen(argv[4], "w");
    for (int k = 0; k <= nbond; k++) if (cnt[k] > 0) fprintf(fo, "%d %.10f\n", k, log(cnt[k]));
    fclose(fo); return 0;
}
