from itertools import permutations

# def solution(expression):
#     answer = 0
# #     iters = ['+', '-', '*']
# #     check = []
# #     for i in range(3):
# #         if iters[i] in expression:
# #             check.append(iters[i])
# #     perms = list(permutations(check, len(check)))
# #     for perm in perms:
# #         for p in perm:
# #             num = ''
# #             prev = ''
# #             idx = 0
# #             for i in range(len(expression)):
# #                 if expression[i].isdigit():
# #                     num += expression[i]
# #                 else:
# #                     if expression[i] == p:
# #                         prev = num
# #                         idx = i - len(prev)
# #                     elif expression[i] != p and prev:
# #                         if p == '+':
# #                             new_num = int(prev) + int(num)
# #                         elif p == '-':
# #                             new_num = int(prev) - int(num)
#                         else:
#                             new_num = int(prev) * int(num)
#                         temp = expression[0:idx] + str(new_num) + expression[idx+len(num)::]
#                         expression = temp
#                         prev = ''
#                     num = ''
#             if prev and num:
#                 if p == '+':
#                     new_num = int(prev) + int(num)
#                 elif p == '-':
#                     new_num = int(prev) - int(num)
#                 else:
#                     new_num = int(prev) * int(num)
#                 temp = expression[0:idx] + str(new_num) + expression[idx + len(prev) + len(num) + 1::]
#                 expression = temp
#         print(expression)
#     return answer

def solution(expression):
    answer = 0
    iters = ['+', '-', '*']
    perms = list(permutations(iters, 3))
    numlist = []
    num = ''
    for i in range(len(expression)):
        if expression[i].isdigit():
            num += expression[i]
        else:
            numlist.append(num)
            numlist.append(expression[i])
            num = ''
        if i == len(expression)-1:
            numlist.append(num)

    for perm in perms:
        temp = numlist.copy()
        for p in perm:
            j = 0
            while j < len(temp):
                if temp[j] == p:
                    prev = temp.pop(j-1)
                    iter = temp.pop(j-1)
                    next = temp.pop(j-1)
                    if p == '+':
                        temp.insert(j-1, str(int(prev) + int(next)))
                    elif p == '-':
                        temp.insert(j - 1, str(int(prev) - int(next)))
                    else:
                        temp.insert(j - 1, str(int(prev) * int(next)))
                else:
                    j += 1
        answer = max(answer, abs(int(temp[0])))
    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))