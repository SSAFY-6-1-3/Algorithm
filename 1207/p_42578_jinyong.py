def solution(clothes):
    answer = 1
    part_list = list(set([part[1] for part in clothes]))
    # 먼저 몇 개의 부위가 있는지부터 리스트에 채워 넣는다.
    for part in part_list:
        # 리스트에 있는 부위별로 총 몇 벌의 있는지 구한다.
        sub_ct = 0
        for cloth in clothes:
            if cloth[1] == part:
                sub_ct += 1
        # 각 부위별 옷의 총 개수를 구하면 해당 수에 1을 더한뒤 answer에 곱한다.
        # 예를 들어 모자 2개, 상의 2개, 하의 2개가 있는 경우를 생각하자
        # 각 부위별로 안 입는다는 선택지도 있으므로 부위별로 총 개수를 1씩 더한다.
        # 그렇게 되면 모자 3개, 상의 3개, 하의 3개 와 같이 되는데
        # 이것을 전부 곱하면 하나도 안 입는 경우부터 각 부위별로 1개씩 입었을 경우인 27가지 경우가 나온다.
        # 우리는 적어도 1벌의 옷을 입어야 하므로 하나도 안 입는 경우 1개를 전체에서 빼주면 되는 것
        answer *= (sub_ct + 1)
    return answer - 1


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
