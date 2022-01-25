K = int(input())
A = [0] * 46
B = [0] * 46
A[1], B[1] = 0, 1
A[2], B[2] = 1, 1
for i in range(3, K+1):
    A[i] = A[i-1] + A[i-2]
    B[i] = B[i-1] + B[i-2]

print(A[K], end=' ')
print(B[K])