
N = 2
# N = int(input())
lst = [0] * (N+2)
lst[1], lst[2] = 1, 2
if N > 2:
    for idx in range(3, N+1):
        lst[idx] = (lst[idx-1] + lst[idx-2]) % 15746

print(lst[N])