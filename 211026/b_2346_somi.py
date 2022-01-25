def pop_bal():
    nums = [i for i in range(N + 1)]
    nums[1] = 0
    cnt = ballons[1]
    now = 1
    print(now, end=' ')
    while any(nums) != 0:
        if cnt > 0:
            while cnt != 0:
                if now + 1 < N + 1:
                    now += 1
                    if nums[now] != 0:
                        cnt -= 1
                elif now + 1 == N + 1:
                    now = 0


        elif cnt < 0:
            while cnt != 0:
                if now - 1 >= 0:
                    now -= 1
                    if nums[now] != 0:
                        cnt += 1
                elif now - 1 < 0:
                    now = N
                    if nums[now] != 0:
                        cnt += 1

        cnt = ballons[now]
        nums[now] = 0
        print(now, end=' ')


N = int(input())
ballons = [0] + list(map(int, input().split()))
pop_bal()

