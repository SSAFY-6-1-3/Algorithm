x = int(input())
stick = 64  # 현재 막대기 길이
now = 0     # 이어붙이고 있는 막대기
cnt = 0     # 부착 횟수

while stick >= 1:
    if now + stick <= x:
        cnt += 1
        now += stick
    stick //= 2

print(cnt)