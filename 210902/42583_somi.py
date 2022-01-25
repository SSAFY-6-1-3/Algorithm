'''
다리를 지나는 트럭
'''


def solution(bridge_length, weight, truck_weights):
    car_index = 0  # 다리를 달릴 차례가 된 차의 index
    bridge = [0] * bridge_length  # 다리 위 상태  도착지 [0, 0, 0, 0, 차1, 차2,] 출발지
    bridge[-1] = truck_weights[car_index]  # 다리 출발지에서 맨 첫번째 차 출발
    time = 1  # 시간
    weight_now = truck_weights[0]  # 현재 다리 위 무게

    while weight_now:  # 현재 다리 위에 차가 있는 동안
        time += 1  # 시간 1초 증가

        if bridge[0] != 0:  # 만약 도착지에 도달한 차가 있다면
            weight_now -= bridge[0]  # 현재 다리 위 무게에서 도착지 도달한 차 무게 빼주기
        bridge.pop(0)
        bridge.append(0)  # 차 한칸씩 이동

        if car_index + 1 < len(truck_weights) and weight_now + truck_weights[car_index + 1] <= weight:  # 다음 차 출발 할 수 있다면
            car_index += 1
            bridge[-1] = truck_weights[car_index]  # 다음차 출발
            weight_now += truck_weights[car_index]  # 다리 위 무게에 해당 차 무게 추가

    return time

print(solution(2, 10, [7, 4, 5, 6]))



# 다른 사람 풀이
## 내가 풀고 싶었던 방식!!!
## 도저히 다리를 달린 시간을 업데이트 할 방법을 모르겠어서 접근 방식이 잘못된줄 알았는데...

def solution(bridge_length, weight, truck_weights):
    t = 0  # time
    on = []  # 도로다리 위 차에 해당하는 정보 (weight, stayed)
    while truck_weights or on:  # 아직 달릴 차가 남아있거나, 다리 위에 차가 남아있는 경우
        for i, e in enumerate(on):  # 다리 위에 차를 움직이기
            on[i] = (e[0], e[1] + 1)  # stayed를 1씩 증가하는 방식!!
        on = list(filter(lambda x: x[1] < bridge_length + 1, on))  # 다리를 다 달린 차는 False로 반환되어 on 리스트에서 빠짐

        weight_sum = 0  # 다리 위 차 무게를 0으로 초기화
        for e in on:  # 다리 위에 있는 차에 대해서
            weight_sum += e[0]  # 차 무게 더해주기

        if truck_weights:  # 대기 중인 차가 있는 경우
            if weight_sum + truck_weights[0] <= weight:  # 무게 제한을 넘지 안흔다면
                on.append((truck_weights.pop(0), 1))  # pop해서 다리 위로 올려주기
        t += 1  # 시간 증가
    return t