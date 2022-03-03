import itertools

def solution(orders, course):
    answer = []
    for num in course:
        menus = {}
        for order in orders:
            order = sorted(list(order))
            com_menu = list(itertools.combinations(order, num))  # 조합
            for menu in com_menu:
                if menu in menus:
                    menus[menu] += 1
                else:
                    menus[menu] = 1
        menus = sorted(menus.items(), key=lambda item: item[1], reverse=True)  # 많이 나온 순으로 정렬
        if menus:  # 없는 경우 고려!!!!
            max_cnt = menus[0][1]
        if max_cnt >= 2:  # 2회 이상만 후보에 작성
            for i in range(len(menus)):
                if menus[i][1] == max_cnt:
                    answer.append(''.join(menus[i][0]))
                else:
                    break
    return sorted(answer)

solution(["XYZ", "XWY", "WXA"], [2,3,4])