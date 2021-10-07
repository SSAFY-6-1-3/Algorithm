target_ch_int = int(input())
# target_ch = []
# for i in str(target_ch_int):
#     target_ch.append(int(i))
#
broken_cnt = int(input())

ok_bts = []  # 고장나지 않은 정상 버튼
if broken_cnt:  # 고장난 버튼 수
    broken_bts = list(map(int, input().split()))
    for i in range(10):
        if i not in broken_bts:
            ok_bts.append(i)
else:  # 고장난 버튼 수가 0이라면,
    ok_bts = [i for i in range(10)]


count = abs(100 - target_ch_int)  # 냅다 위, 아래로만 누르는 경우
for ch in range(1000001):  # 100만까지 순회
    for j in range(len(str(ch))):
        if int(str(ch)[j]) not in ok_bts:  # 해당 버튼을 만들 지 못하는 경우
            break
        elif len(str(ch)) - 1 == j:  # 끝자리까지 만들 수 있는 경우
            count = min(count, abs(ch - target_ch_int) + len(str(ch)))  # 최소값을 저장
print(count)


