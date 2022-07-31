
N = int(input())
orgs = list(map(int, input().split()))
fakes = [0] * N
fakes
for i in range(1, N):
    if i % 2:       # 이미 한번 쓴거,         밑장 내가 가지기,      밑장 주기
        fakes[i] = max(fakes[i - 2] + orgs[i], orgs[i - 1] + orgs[-1])
        if i < N-1:
            fakes[i] = max(fakes[i], orgs[i-1] + orgs[i+1])
    else:
        orgs[i] += orgs[i - 2]

print(orgs, fakes)
print(max(orgs[N-2], fakes[N-3]))