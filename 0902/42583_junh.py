def solution(bridge_length, weight, truck_weights):
    sec = 0
    truck_now = [] # 다리 위의 트럭을 [무게, 위치]의 방식으로 저장할 큐

    while truck_weights or truck_now: # 트럭 목록이나 다리 위에 트럭이 남아있는 동안
        sec += 1 # 시간 +1
        for truck in truck_now: # 다리위 트럭들의 위치를 +1
            truck[1] += 1

        if truck_now and truck_now[0][1] == bridge_length: # 다리 위에 트럭이 있고, 맨 앞의 트럭이 다리 끝에 다다르면
            truck_now.pop(0) # 그 트럭을 빼준다
        # 대기 트럭이 있고, 다리 길이에 여유가 있으며, 다리 위 트럭 무게의 합에 대기 트럭 하나를 더해도 수용 가능하면
        if truck_weights and bridge_length > len(truck_now) and weight >= sum(truck_now[i][0] for i in range(len(truck_now))) + truck_weights[0]:
            truck_now.append([truck_weights.pop(0), 0]) # 맨 앞의 대기 트럭을 다리 위에 올린다.

    return sec



print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))