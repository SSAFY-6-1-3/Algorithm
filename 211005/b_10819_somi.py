def find_max(p):
    global max_v
    total = 0
    for i in range(N-1):
        total += abs(p[i] - p[i + 1])

    if total > max_v:
        max_v = total


def permutation(N, k):  # 배열의 k번째 칸 채우기 (줄세우기)
    if k == N:
        find_max(p)     # 다 완성되면 max 값이 되는 지 확인

    else:
        for i in range(N):
            if not used[i]:  # 아직 사용되지 않은 인덱스이면
                p[k] = A[i]  # 해당 인덱스 값을 배열에 넣고
                used[i] = 1  # 사용했다고 표시
                permutation(N, k+1)  # 배열의 다음 자리를 채우러 이동
                used[i] = 0  # 초기화


N = int(input())
A = list(map(int, input().split()))

used = [0] * N  # A열의 해당 인덱스 값을 사용했는 지 여부
p = [0] * N     # 새로 만들어질 배열
max_v = 0
permutation(N, 0)
print(max_v)

