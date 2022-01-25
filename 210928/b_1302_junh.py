import sys
input = sys.stdin.readline
N = int(input())
dict = {}

for _ in range(N):
    a = input()
    if dict.get(a):
        dict[a] += 1
    else:
        dict[a] = 1
print(dict)
max_n = max(dict.values())
print(max_n)
max_li = []
for key in dict:
    if dict[key] == max_n:
        max_li.append(key)

print(min(max_li))

