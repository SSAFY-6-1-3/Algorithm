'''
i = 2*(i-1) + (i-2) 점화식 이용
'''
N = int(input())
if N > 2:
    lst = [0] * (N+1)
    lst[1], lst[2] = 3, 7
    for i in range(3, N+1):
        lst[i] = (2*lst[i-1]+lst[i-2]) % 9901
    print(lst[N])
else:
    if N == 1:
        print(3)
    else:
        print(7)