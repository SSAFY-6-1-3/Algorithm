T = int(input())
answer = [0] + []
for _ in range(1, T + 1):
    A, B, C, D = map(int, input().split())
    L = min(B, D) - max(A, C)
    ans = 0
    if L > 0:
        ans = L
    answer.append(ans)

for i in range(1, len(answer)):
    print('#{} {}'.format(i, answer[i]))


'''
시간 초과
    X = {i for i in range(A, B + 1)}
    Y = {j for j in range(C, D + 1)}
    L = len(X & Y)
    ans = 0
    if L:
        ans = L - 1

'''