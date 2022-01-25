def move(n, now, mid, goal):
    if n==1:
        print('{} {}'.format(now, goal))
        return

    move(n-1, now, goal, mid)
    print('{} {}'.format(now, goal))
    move(n-1, mid, now, goal)

n = int(input())

hanoi = [0]*(n+1)
hanoi[1] = 1

for i in range(2, n+1):
    hanoi[i] = hanoi[i-1]*2 +1
print(hanoi[n])

move(n, 1, 2, 3)


