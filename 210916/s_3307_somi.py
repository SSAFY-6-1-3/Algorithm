import sys
sys.stdin = open('s_3307_input.txt')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    dp = [1] * N
    for n in range(N):      # 비교할 숫자의 인덱스를 n
        for i in range(n):  # 비교할 숫자보다 앞에 있는 숫자들과 하나씩 비교
            if numbers[i] < numbers[n]:  # 만약 작은 숫자가 앞에 있다면
                dp[n] = max(dp[n], dp[i] + 1)  # max값을 넣기

    print('#{} {}'.format(tc, max(dp)))



    
