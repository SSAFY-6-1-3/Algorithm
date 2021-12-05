def solution(clothes):
    answer = 0

    c_dic = {}
    for cloth in clothes:
        c_type = cloth[1]
        if c_dic.get(c_type) == None:
            c_dic[c_type] = 1
        else:
            c_dic[c_type] +=1
    c_li = list(c_dic.values())

    yame = True                 # 1번 tc 처리용. 다른 방법 찾아볼 것.
    for c in c_li:
        if c>1:
            yame = False
    if yame:
        return 2**len(c_li) -1

    def dfs(start, value, able_depth):
        nonlocal answer
        if not able_depth :
            answer += value
            return
        for i in range(start+1, len(c_li)):
            dfs(i, value*c_li[i], able_depth-1)

    for choices in range(1, len(c_li)+1):
        dfs(-1, 1, choices)

    return answer

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))


# def copy_solution(clothes):
#     answer = 0
#     closet = {}
#     count = 1
#     for cloth in clothes:
#         key = cloth[1]
#         value = cloth[0]
#         closet[key].append(value)
#
#     for key in closet:
#         count = count * (len(closet[key]) + 1)
#     answer = count - 1
#     return answer