import sys
sys.stdin=open('input.txt')

def find_idx(num):
    for idx in range(300):
        if lst[idx] > num:
            return idx-1


T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    lst = [1] + [0] * 300               # x = 1위치의 값 구하기 (최대값 300)
    for i in range(1, 300):
        lst[i] = lst[i-1] + i-1

    a_idx = find_idx(a)                 # 구하려는 숫자가 포함되는 대각선 구하기
    b_idx = find_idx(b)

    cnt = a - lst[a_idx]                # 숫자의 위치 구하기 (x = 1위치에서 대각선으로 이동)
    ay, ax = a_idx-cnt, cnt+1
    cnt = b - lst[b_idx]
    by, bx = b_idx - cnt, cnt + 1

    cx, cy = ax+bx, ay+by
    result = lst[cy+cx-1]               # 위치를 다시 숫자로 바꾸기
    result += cx-1                      # x=1 위치와 비교 (cx-1 차이만큼 이동)
    print('#{} {}'.format(tc, result))

