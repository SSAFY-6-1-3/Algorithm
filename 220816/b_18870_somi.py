N = int(input())
points = list(map(int, input().split()))
numbers_list = sorted(list(set(points)))
numbers_dict = dict()

for i in range(len(numbers_list)):
    numbers_dict[numbers_list[i]] = i

for p in points:
    print(numbers_dict[p], end=' ')
