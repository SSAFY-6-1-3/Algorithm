def solution(info, query):
    info = list(i.split() for i in info)
    query = list(i.replace('and ', '').split() for i in query)
    ans = []

    info_dict = dict()
    for i in info:

    for q in query:
        pass
    return ans

'''
# 효율성 실패
def solution(info, query):
    info = list(i.split() for i in info)
    query = list(i.replace('and ', '').split() for i in query)
    ans = []
    for q in query:
        filter_tmp = list(filter(lambda i: int(i[-1]) >= int(q[-1]), info))
        for i in range(4):
            if q[i] != '-':
                filter_tmp = list(filter(lambda tmp: tmp[i] == q[i], filter_tmp))
        ans.append(len(filter_tmp))
    return ans
'''


a = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
b = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(a, b))

