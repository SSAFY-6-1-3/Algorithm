# 누적합 사용!
N = int(input())
cards = list(map(int, input().split()))
first = [0]
second = [0]
for i in range(N//2):
    first.append(first[-1] + cards[2*i])
    second.append(second[-1] + cards[2*i+1])
ans = first[-1]
# 내꺼 밑장빼기
for i in range(N//2):
    temp1 = first[i] + second[-1] - second[i]
    ans = max(ans, temp1)
# 상대방꺼 밑장빼기
for j in range(N//2):
    temp2 = first[j+1] + second[-2] - second[j]
    ans = max(ans, temp2)
print(ans)