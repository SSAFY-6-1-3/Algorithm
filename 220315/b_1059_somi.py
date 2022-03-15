def combination(start, end):
    cnt = 0
    for i in range(start + 1, end - 1):
        for j in range(i + 1, end):
            if n in range(i, j + 1):
                cnt += 1
    return cnt


L = int(input())
S = [0] + list(map(int, input().split()))  # n이 집합 S에서 가장 작은 수보다도 작을 수 있으니, 0 추가
n = int(input())

S.sort()

if n in S:
    print(0)
else:
    start = 0
    end = 1
    ans = 0
    while end <= L:
        ans += combination(S[start], S[end])
        start += 1
        end += 1
    print(ans)
