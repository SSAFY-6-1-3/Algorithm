"""
sum 함수 쓰면 런타임 에러
"""
from collections import deque
bridge_length = 5
weight = 5
truck_weights = [1,1,1,1,1,2,2]

bridge = [0] * bridge_length
bridge = deque(bridge)          # 다리 위 트럭
trucks = deque(truck_weights)   # 대기트럭
cnt = 0

while bridge:                                   # bridge 리스트가 안 빌 때까지 반복
    if trucks:                                  # 대기트럭이 있다면 계속 반복
        truck = trucks.popleft()                # 가장 처음 대기 트럭
        on_bridge = sum(bridge)                 # 다리 위에 올라가있는 트럭 무게
        if (weight - on_bridge) >= truck:       # 다리 위에 트럭이 올라갈 수 있다면
            bridge.popleft()                    # 다리 위 맨 앞에 트럭 빼고
            bridge.append(truck)                # 대기 트럭 하나 다리 위에 올리기
            cnt += 1                            # 1초 더하기
        else:                                   # 다리 위에 트럭이 올라갈 수 없다면 올라갈 수 있을 때까지 다리 위 트럭 빼기
            while True:
                    on_bridge -= bridge.popleft()           # 트럭 하나 빠질 때마다 새로운 트럭이 올라갈 수 있는지 확인
                    if (weight - on_bridge) >= truck:
                        break
                    bridge.append(0)                        # 못 올라간다면 0 넣어주기
                    cnt += 1
            bridge.append(truck)                            # 올라갈 수 있으면 break하고 트럭 올리기
            cnt += 1
    else:
        cnt += bridge_length                    # 더이상 대기버스가 없다면 다리 위 버스들 모두 더하기
        bridge = []
print(cnt)
