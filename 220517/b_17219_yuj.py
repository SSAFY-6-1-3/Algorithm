N, M = map(int, input().split())
dic = dict()
for _ in range(N):
    site, pw = map(str, input().split())
    dic[site] = pw

for _ in range(M):
    print(dic[input()])