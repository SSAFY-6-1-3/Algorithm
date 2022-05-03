a = int(input())
b = list(map(int, input().split(" ")))
b.sort(reverse=False)
total_time = 0
temp = 0
for i in range(a):
    temp += b[i]
    total_time += temp
print(total_time)