A, B = map(int, input().split())

# 시간초과...

# if A == 1 or B == 1:
#     print(max(A, B))
#
# else:
#     max_num = A * B
#
#     A_multis = []
#     B_multis = []
#
#     for i in range(1, max_num):
#         A_tmp = A * i
#         A_multis.append(A_tmp)
#
#         B_tmp = B * i
#         B_multis.append(B_tmp)
#
#         if A_tmp in B_multis:
#             print(A_tmp)
#             break
#
#         if B_tmp in A_multis:
#             print(B_tmp)
#             break

import math
print(math.lcm(A, B))