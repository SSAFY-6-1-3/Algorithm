N, K = map(int, input().split())

li = [i for i in range(1, N+1)]
answer = []
now = -1
while li:
    now = (now+K)%len(li)
    answer.append(li.pop(now))
    now-=1
answer = map(str, answer)
print('<', end='')
print(', '.join(answer), end='')
print('>')