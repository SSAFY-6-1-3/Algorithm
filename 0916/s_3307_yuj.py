import sys
sys.stdin = open('s_3307_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    sum_lst = [1] + [0] * (N-1)                 # 증가 수열 개수 저장해놓을 리스트
    max_idx = 0

    for i in range(1, N):                       # 현재 위치 이전까지 증가 수열 개수 확인하기
        for j in range(i-1,-1,-1):
            if lst[j] < lst[i] and sum_lst[j] > sum_lst[i]:  # 현재값보다 작고, 증가 수열 개수가 클 때만
                sum_lst[i] = sum_lst[j]                      # 변경시키기

        sum_lst[i] += 1                         # 자기 자신도 길이에 추가하기


    print('#{} {}'.format(tc,max(sum_lst)))

