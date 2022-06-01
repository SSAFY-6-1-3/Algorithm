N, M = map(int, input().split())
site = dict()
for _ in range(N):
    url, password = input().split()
    site[url] = password

for _ in range(M):
    url = input()
    print(site[url])