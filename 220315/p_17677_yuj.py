
def solution(str1, str2):
    lst_str1 = []
    lst_str2 = []
    for idx in range(len(str1) - 1):
        temp1 = str1[idx:idx + 2]
        if temp1.isalpha():
            lst_str1.append(temp1.lower())

    for idx in range(len(str2) - 1):
        temp2 = str2[idx:idx + 2]
        if temp2.isalpha():
            lst_str2.append(temp2.lower())

    if not lst_str1 and not lst_str2:
        return 65536

    union = len(lst_str1) + len(lst_str2)
    intersection = 0
    for s in lst_str1:
        if s in lst_str2:
            intersection += 1
            lst_str2.remove(s)
    union -= intersection

    answer = (intersection / union) * 65536
    return int(answer)

print(solution('FRANCE', 'french'))
print(solution('handshake','shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))
print(solution('A+C', 'DEF'))
