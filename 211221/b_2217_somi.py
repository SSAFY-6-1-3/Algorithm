N = int(input())
ropes = [0] + sorted((int(input()) for _ in range(N)), reverse=True)  # 최대 중량을 내림차순으로 정렬

weight = [0] * (N + 1)
for i in range(1, N + 1):
    weight[i] = i * ropes[i]  # 중량 * 인덱스 만큼을 버틸 수 있음

print(max(weight))