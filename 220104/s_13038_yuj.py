import sys
sys.stdin=open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    week = list(map(int, input().split()))

    answer = n * 7
    for idx in range(7):                    # 1이 나오는 요일 모두에서 시작해보기
        result = 0
        study = 0
        if week[idx]:
            while study < n:
                if week[idx % 7]:
                    study += 1
                result += 1
                idx += 1
            answer = min(result, answer)

    print('#{} {}'.format(tc, answer))