def makeSet(string):
    cnt = 0
    dict = {}
    for i in range(len(string) - 1):
        tmp = string[i] + string[i + 1]
        if tmp.isalpha():
            if tmp in dict:
                dict[tmp] += 1
            else:
                dict[tmp] = 1
            cnt += 1
    return dict, cnt

def solution(str1, str2):
    string1, cnt1 = makeSet(str1.upper())
    string2, cnt2 = makeSet(str2.upper())

    intersection = 0
    total = cnt1 + cnt2
    if total:
        for char in string1:
            if char in string2:
                intersection += min(string1[char], string2[char])

        union = total - intersection
        answer = int((intersection / union) * 65536)

    else:
        answer = 65536

    return answer

print(solution('A+C', 'DEF'))