N = int(input())
time = list(map(int, input().split()))

person = 0
total_time = 0

for i in range(N):
    for j in range(i, N):
        if time[i] > time[j]:
            time[i], time[j] = time[j], time[i]
    person = time[i] + person
    total_time += person

print(total_time)
