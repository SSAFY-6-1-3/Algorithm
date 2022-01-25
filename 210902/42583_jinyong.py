def solution(bridge_length, weight, truck_weights):
    passed_truck = []
    truck_ct = len(truck_weights)
    move_distance = [0] * truck_ct
    on_bridge = 0
    need_time = 1
    first = last = 0
    while first < truck_ct or on_bridge:  # 건너야 하는 트럭이 있거나 건너는 중인 트럭이 있으면 반복

        if last < truck_ct and on_bridge + truck_weights[last] <= weight:
            on_bridge += truck_weights[last]
            last += 1

        for i in range(first, last):
            move_distance[i] += 1
            if move_distance[i] == bridge_length:
                passed_truck.append(truck_weights[i])
                first += 1
                on_bridge -= truck_weights[i]

        need_time += 1

    return need_time


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
