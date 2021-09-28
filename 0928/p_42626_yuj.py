import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)                             # 최소 힙 생성
    while scoville[0] < K and len(scoville) >= 2:
        min_1 = heapq.heappop(scoville)                 # 힙에서 가장 작은 원소 삭제
        min_2 = heapq.heappop(scoville)
        new = min_1 + min_2*2
        cnt += 1
        heapq.heappush(scoville, new)                   # 힙에 새로운 값 추가

    if scoville[0] < K:                                 # 모든 음식의 스코빌 지수가 K 이하일 때
        return -1
    return cnt


scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))