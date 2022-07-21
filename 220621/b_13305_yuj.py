N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
minv = 1000000000
answer = 0
for i in range(N-1):
    minv = min(minv, prices[i])
    answer += distances[i] * minv

print(answer)