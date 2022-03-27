def workout(days, w):
    global cnt
    if days == N:
        if w >= 500:
            cnt += 1
        return

    if w < 500:
        return

    for i in range(len(kits)):
        if not done[i]:
            done[i] = True
            workout(days + 1, w - K + kits[i])
            done[i] = False




N, K = map(int, input().split())
kits = list(map(int, input().split()))
cnt = 0
done = [False] * N
for i in range(len(kits)):
    kit = kits[i]
    done[i] = True
    workout(1, 500 - K + kit)
    done[i] = False

print(cnt)