import sys
# from itertools import permutations
sys.stdin=open('input.txt')
'''
처음 풀이
'''
# def turn():
#     minv = abs(N - 100)
#
#     if len(button) == 0:
#         return minv
#     if N == 98:
#         return 2
#     elif N == 99 or N == 101:
#         return 1
#
#     for i in range(abs(N - 100)):                    # 목표 채널에서 전,후로 1씩 채널을 돌리면서 이동 채널 목록 안에 있는지 확인
#         x, y = str(N - i), str(N + i)
#         if N - i <= 0:                          # 0번 채널보다 작아질 경우 0번으로 생각
#             x = '0'
#         if x in channel:
#             if i + len(x) < minv:
#                 minv = i + len(x)
#                 break
#         if y in channel:
#             if i + len(y) < minv:
#                 minv = i + len(y)
#                 break
#     return minv
#
# button = []
# channels = []
# channel = []
# for n in range(10):                                 # 누를 수 있는 버튼 구하기
#     if n not in broken_button:
#         for _ in range(6):
#             button.append(str(n))
#
# for _ in range(1, 8):                               # 누를 수 있는 버튼들로 이동할 수 있는 채널 모두 구하기
#     channels += list(permutations(button, _))
#
# for c in channels:
#     channel.append(''.join(c))
#
# print(turn())

def turn():
    minv = abs(N - 100)
    for num in range(1000000):                      # 500000번으로 이동해야할 경우, 최악의 경우 500000-100=499900이므로
        for n in str(num):                          # 500000 + 4999900번에서 오만번으로 내려올 경우까지 생각
            if n not in button:
                break
        else:
            if len(str(num))+abs(N-num) < minv:
                minv = len(str(num))+abs(N-num)
    return minv

N = int(input())
num = int(input())
if num > 0:
    broken_button = list(map(int, input().split()))
else:
    broken_button = []
button = []
for n in range(10):                                 # 누를 수 있는 버튼 구하기
    if n not in broken_button:
        button.append(str(n))

print(turn())