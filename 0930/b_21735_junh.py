

def rolling(now, snow, cnt):
    global largest
    if cnt > M:
        return
    if snow > largest:
        largest = snow
    if now <= N-1:
        rolling(now + 1, snow + yard[now + 1], cnt + 1)
    if now <= N-2:
        rolling(now+2, snow//2 + yard[now+2], cnt + 1)



N, M = map(int, input().split())
yard = [0] + list(map(int, input().split()))
largest = 0

rolling(0, 1, 0)
print(largest)
