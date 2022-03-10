def solution(s):
    answer = []
    dic = {}
    num = ''
    ast = ['}','{',',']
    for st in s:
        if st in ast:
            if num:
                if num not in dic:
                    dic[num] = 1
                else:
                    dic[num] += 1
            num = ''
        else:
            num += st

    for l in range(len(dic), 0, -1):
        for number in dic:
            if dic[number] == l:
                answer.append(int(number))

    return answer