K = int(input())
monitor = [[0, 0] for _ in range(K + 1)]
monitor[0][0] = 1

# A => B, B => BA
for i in range(1, K + 1):
    a, b = monitor[i - 1]
    monitor[i][0], monitor[i][1] = b, a + b

print(*monitor[K])
