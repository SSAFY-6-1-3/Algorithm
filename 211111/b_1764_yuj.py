import sys
sys.stdin=open('input.txt')

# 딕셔너리 사용
a, b = map(int, input().split())
dict = {}
names = set()
for _ in range(a):
    dict[input()] = 0

for _ in range(b):
    name = input()
    if name in dict:
        dict[name] += 1

results = []
for name in dict:
    if dict[name]:
        results.append(name)

results.sort()
print(len(results))
for result in results:
    print(result)
    

# set 사용    
# a, b = map(int, input().split())
# lst = set()
# names = set()
# for _ in range(a):
#     lst.add(input())
# 
# for _ in range(b):
#     name = input()
#     if name in lst:
#         names.add(name)
# 
# results = sorted(names)
# print(len(results))
# for result in results:
#     print(result)