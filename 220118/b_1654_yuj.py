# def binary_search(s, e):
#     global result
#
#     mid = (s+e) // 2
#     cnt = 0
#     for lan in lans:
#         cnt += lan // mid
#
#     if cnt == N:
#         return mid
#
#     if s == e-1:
#         return s
#
#     if s <= e:
#         if cnt < N:
#             return binary_search(0, mid-1)
#         else:
#             return binary_search(mid+1, e)
#
#
# K, N = map(int, input().split())
# lans = [int(input()) for _ in range(K)]
#
# if min(lans) == max(lans):
#     print(lans[-1])
# else:
#     print(binary_search(0, max(lans)))

K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]
s = 1
e = max(lans)
result = 1
while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for lan in lans:
        cnt += lan // mid

    if cnt < N:
        e = mid - 1
    else:
        result = max(result, mid)
        s = mid + 1

print(result)