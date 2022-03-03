import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
start = 0
end = max(trees)

while start <= end:
    cut = (start + end) // 2
    #total = sum(map(lambda x: max(0, x - cut), trees))
    total = 0
    for tree in trees:
        if tree - cut > 0:
            total += tree - cut
            if total > M:  # 초과 되는 경우 break! 이부분 없으면 시간초과
                break
    if total < M:
        end = cut - 1
    else:
        start = cut + 1

print(end)