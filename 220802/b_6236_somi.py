def withdraw(money):
    cnt = 0  # 인출 횟수
    now = 0  # 현재 가진 돈

    for n in need:
        if n > money:  # mid 가 부족한 경우
            return 0

        elif n > now:  # 더 인출해야 하는 경우
            cnt += 1
            now = money

        now -= n  # 현재 가진 돈에서 필요한 액수 사용
    return cnt


N, M = map(int, input().split())
need = list(int(input()) for _ in range(N))

total = sum(need)
K, left, right = total, 0, total

while left <= right:
    mid = (left + right) // 2
    cnt = withdraw(mid)

    if not cnt:  # 돈 부족한 날 있으면 인출액 늘리기
        left = mid + 1

    else:
        if cnt <= M:
            right = mid - 1
            if mid < K:
                K = mid

        elif cnt > M:
            left = mid + 1

print(K)



