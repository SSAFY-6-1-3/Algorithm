import sys
sys.stdin=open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, list(input())))
    people, result = 0, 0                   # 현재 박수치는 인원, 필요한 인원

    for idx in range(len(lst)):
        if lst[idx]:                        # 박수칠 사람들이 있으면 확인
            minus = idx - people
            if minus > 0:                   # 지금 박수치고 있는 사람들이 적다면
                result += minus             # 고용할 사람들 추가
                people += minus + lst[idx]  # 고용할 사람들 + 박수칠 사람들 추가
            else:
                people += lst[idx]

    print('#{} {}'.format(tc, result))
