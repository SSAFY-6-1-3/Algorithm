import sys
sys.stdin = open('s_1486.txt.')

def make_tower():
    min = sum(H)  # 직원 모두가 탑을 쌓은 경우를 min으로
    for i in range(1 << N): # 부분집합 구하기
        temp = []  # 부분집합 잠시 저장할 리스트
        for j in range(N):
            if i & (1 << j):
                temp.append(H[j])
        if sum(temp) >= B: # 지금 만든 탑(부분집합) 높이가 B 보다 높거나 같을 때,
            if sum(temp) < min:  # min값 갱신
                min = sum(temp)
    return min

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))

    ans = make_tower() - B
    print('#{} {}'.format(tc, ans))