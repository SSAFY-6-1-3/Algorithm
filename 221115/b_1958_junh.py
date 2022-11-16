A = ' ' + input()
B = ' ' + input()
C = ' ' + input()

lcs = [[[0 for _ in range(len(C))] for _ in range(len(B))] for _ in range(len(A))]

for a in range(1, len(A)):
    for b in range(1, len(B)):
        for c in range(1, len(C)):
            if A[a] == B[b] and B[b] == C[c]:
                lcs[a][b][c] = lcs[a-1][b-1][c-1] + 1
            else:
                lcs[a][b][c] = max(lcs[a-1][b][c], lcs[a][b-1][c], lcs[a][b][c-1])

print(max(lcs[-1][-1]))