def walk():
    q = [(home_r, home_c)]
    flag = 'sad'
    while q:
        now_r, now_c = q.pop()
        if abs(now_r - festival_r) + abs(now_c - festival_c) <= 1000:
            flag = 'happy'
            break

        for i in range(n):
            if not visited[i]:
                next_r, next_c = conv[i]
                if abs(now_r - next_r) + abs(now_c - next_c) <= 1000:
                    q.append((next_r, next_c))
                    visited[i] = True

    return flag

T = int(input())
for _ in range(T):
    n = int(input())

    home_r, home_c = map(int, input().split())

    conv = []
    for _ in range(n):
        r, c = map(int, input().split())
        conv.append((r, c))

    festival_r, festival_c = map(int, input().split())
    visited = [False for _ in range(n)]  # 편의점 visit 처리
    print(walk())