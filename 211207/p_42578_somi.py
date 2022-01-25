def solution(clothes):
    clothes_dict = {}
    for value, key in clothes:
        if key not in clothes_dict:
            clothes_dict[key] = 1
        else:
            clothes_dict[key] += 1

    answer = 1
    for i in clothes_dict.values():
        answer *= (i + 1)

    return answer - 1


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))

