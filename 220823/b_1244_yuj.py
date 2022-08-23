N = int(input())
switches = [0] + list(map(int, input().split()))
num = int(input())
for _ in range(num):
    student, switch = map(int, input().split())
    if student == 1:
        for i in range(1, N // switch + 1):
            switches[switch * i] = 1 - switches[switch * i]

    else:
        length = min(switch, N-switch+1)
        switches[switch] = 1 - switches[switch]
        for j in range(1, length):
            l, r = switches[switch-j], switches[switch+j]
            if l != r:
                break
            else:
                switches[switch-j] = 1 - l
                switches[switch+j] = 1 - r

for k in range(1, N+1):
    print(switches[k], end=" ")
    if k % 20 == 0:
        print()
