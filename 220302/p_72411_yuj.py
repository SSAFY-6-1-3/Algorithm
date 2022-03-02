# collections 의 Coutner 사용하면 좀 더 간편
from itertools import combinations

def solution(orders, course):
    answer = []
    foods = dict()

    for num in course:
        for order in orders:
            for new in list(combinations(sorted(order), num)):  # 메뉴가 알파벳 순서대로 저장되도록 sorted
                if new in foods:
                    foods[new] += 1
                else:
                    foods[new] = 1

    menus = [[] for _ in range(21)]
    cnt = [[] for _ in range(21)]
    for food in foods:
        if foods[food] >= 2:
            if cnt[len(food)]:
                if cnt[len(food)] < foods[food]:
                    cnt[len(food)] = foods[food]
                    menus[len(food)] = [food]

                elif cnt[len(food)] == foods[food]:
                    menus[len(food)].append(food)
            else:
                cnt[len(food)] = foods[food]
                menus[len(food)] = [food]

    for c in course:
        for menu in menus[c]:
            answer.append(''.join(menu))

    answer.sort()

    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))