# 블루레이 하나의 크기를 이분탐색
# 블루레이 크기를 정해두고, 블루레이에 몇 개의 강의가 들어갈 수 있는지 확인(cnt)
N, M = map(int, input().split())
time = list(map(int, input().split()))
ans = 10000 * N
def check(num):
    global ans

    cnt = 1
    temp = num
    for t in time:
        if temp >= t:
            temp -= t
        else:
            cnt += 1
            temp = num
            temp -= t

    return cnt

s = max(time)
e = sum(time)
maxv = max(time)

while s <= e:
    mid = (s+e) // 2
    cnt = check(mid)
    if cnt > M:
        s = mid+1
    else:
        e = mid-1
        ans = min(ans, mid)

print(ans)