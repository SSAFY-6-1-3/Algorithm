from collections import deque

T = int(input())
for _ in range(T):
    commands = input()
    N = int(input())
    lst = input()[1:-1].split(',')
    nums = deque(lst)
    if lst == ['']:
        nums = []
    else:
        nums = deque(list(map(int, lst)))
    idx = 0
    flag = 1
    for command in commands:
        if command == 'R':
           if not idx:
               idx = -1
           else:
               idx = 0
        elif command == "D":
            if not nums:
                print('error')
                flag = 0
                break
            elif idx == 0:
                nums.popleft()
            else:
                nums.pop()
        if not flag:
            break
    else:
        if idx == -1:
            ans = str(list(nums)[::-1]).replace(' ', '')
        else:
            ans = str(list(nums)).replace(' ','')
        print(ans)