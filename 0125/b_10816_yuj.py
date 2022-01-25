# def binary_search(num, flag):
#     l, r = 0, N - 1
#     ans = 0
#     while l <= r:
#         mid = (l+r) // 2
#         if cards[mid] > num:
#             r = mid - 1
#         elif cards[mid] < num:
#             l = mid + 1
#         else:
#             ans = mid
#             if flag:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#     return ans
#
#
# N = int(input())
# cards = sorted(list(input().split()))
# M = int(input())
# nums = list(input().split())
#
# for num in nums:
#     start = binary_search(num, 0)
#     end = binary_search(num, 1)
#
#     print(end-start, end=' ')

N = int(input())
cards = sorted(list(input().split()))
M = int(input())
nums = list(input().split())
dic = dict()

for card in cards:
    if card in dic:
        dic[card] += 1
    else:
        dic[card] = 1

for num in nums:
    if num in dic:
        print(dic[num], end=' ')
    else:
        print(0, end=' ')