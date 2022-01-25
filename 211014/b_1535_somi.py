def thank(i, p, j):
    global joy
    if p <= 0:
        return
    if j > joy:
        joy = j

    for friend in range(i, N):
        if not visited[friend]:
            visited[friend] = 1
            thank(friend, p - L[friend], j + J[friend])
            visited[friend] = 0


N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

visited = [0] * N  # 해당 인덱스 사람을 만났는 지
power = 100  # 체력
joy = 0      # 기쁨

for i in range(N):  # i번째 사람 만나러 가기
    visited[i] = 1
    thank(i, 100 - L[i], J[i])
    visited[i] = 0
print(joy)