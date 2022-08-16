from collections import deque

T = int(input())
for _ in range(T):
    A, B = map(str, input().split())
    # visited 확인
    nums = [0] * 10000
    ans = ''
    nums[int(A)] = 1
    q = deque([(A, '')])
    while deque:
        now, reg = q.popleft()

        if int(now) == int(B):
            print(reg)
            break
        # 4글자로 맞춰주기
        if len(now) < 4:
            zero = '0' * (4 - len(now))
            now = zero + now

        if int(now) > 0:
            if not nums[int(now)-1]:
                nums[int(now) - 1] = 1
                q.append((str(int(now)-1), reg+'S'))
        else:
            if not nums[9999]:
                nums[9999] = 1
                q.append((str(9999), reg+'S'))

        new_L = now[1:4] + now[0]
        new_R = now[-1] + now[0:3]
        new_D = str((int(now) * 2))[-4::]

        if not nums[int(new_L)]:
            nums[int(new_L)] = 1
            q.append((new_L, reg+'L'))
        if not nums[int(new_R)]:
            nums[int(new_R)] = 1
            q.append((new_R, reg+'R'))

        if not nums[int(new_D)]:
            nums[int(new_D)] = 1
            q.append((new_D, reg+'D'))