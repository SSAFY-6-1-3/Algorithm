import sys

input = sys.stdin.readline

def bin_search(l, r, bd):
    mid = (l+r) //2
    if l>r : return False
    if heard[mid] == bd:
        return True
    if heard[mid] < bd:
        return bin_search(mid+1, r, bd)
    return bin_search(l, mid-1, bd)


n, m = map(int, input().split())
heard = []
for _ in range(n):
    heard.append(input().strip())
heard.sort()

dbj = []
for _ in range(m):
    bd = input().strip()
    if bin_search(0, len(heard)-1, bd):
        dbj.append(bd)

dbj.sort()
print(len(dbj))
for db in dbj:
    print(db)
print(dbj)