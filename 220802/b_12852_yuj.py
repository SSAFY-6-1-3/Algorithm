def cal(num, lst):
    global ans

    if num < 1 or len(lst) > len(ans):
        return

    if num == 1:
        if len(ans) > len(lst):
            ans = lst
        return

    if not num % 3:
        cal(num//3, lst+[num//3])
    if not num % 2:
        cal(num // 2, lst + [num // 2])
    if num > 1:
        cal(num-1, lst+[num-1])

N = int(input())
ans = [0] * 2 * N
cal(N, [N])
print(len(ans)-1)
print(*ans)
