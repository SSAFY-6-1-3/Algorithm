import sys

input = sys.stdin.readline

def check(cnt, rst):        # 재귀를 통한 브루트포스
    global n_min

    if rst != '':               # 처음 함수에서는 int('')하면 에러가 나니 생략
        press = cnt             # 숫자를 누른 횟수 + (+, -)를 누른 횟수
        press += abs(int(N) - int(rst))
        if n_min > press:
            n_min = press

    if cnt > length:            # cnt가 채널의 length보다 1 클 때는 위에서 검사를 실행, 그 외엔 실행이 안 된다
        return

    if cnt < length:            # 카운트가 적을 때는 가지치기를 해준다 (cnt==length 때는 인덱스 문제로 불가)
        l, r = '', ''
        for i in range(len(left)):              # 눌러야하는 숫자보다 크고 가까운 수 하나
            if int(left[i]) > int(N[cnt]):
                r = left[i]
                break
        for i in range(len(left)):              # 작고 가까운 수
            if int(left[-1-i]) < int(N[cnt]):
                l = left[-1-i]
                break
        nums = [l, r, left[0], left[-1]]        # 누를 수 있는 가장 큰 수, 누를 수 있는 가장 작은 수

        if N[cnt] in left:                      # 눌러야 하는 수
            nums.append(N[cnt])
        if cnt == 0 and left[0] == '0' and len(left)>1: # 제일 처음 재귀 때 시작숫자가 0이면
            nums.append(left[1])                        # 그 다음 숫자도 추가해줌

        nums = list(set(nums))                          # 중복되는 숫자를 없애기 위해 set 담갔다 빼기
        nums.sort()                                     # 정렬
    else:                               # cnt==length 일때는 그냥 left 그대로 사용
        nums = left

    for num in nums:                    # 누를 수 있는 번호들을 누르고 재귀 호출
        check(cnt + 1, rst + num)   # 카운트 1 늘리고, 누를 숫자 번호,


N = input().strip()
M = int(input())
li = []
if M:
    li = list(map(int, input().split()))

left = []               # 사용 가능한 번호들
for n in range(10):
    if n not in li:
        left.append(str(n))

length = len(N)
n_min = abs(int(N)-100)         # +, -만 사용했을때 필요한 횟수
if left:
    check(0, '')             # 재귀를 통해 브루트포스 순회
print(n_min)

'''
https://www.acmicpc.net/board/view/31853 반례들
'''