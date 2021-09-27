import heapq # 리스트를 힙처럼 사용하게 해주는 라이브러리 기능

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # scolville을 heap 구조로 바꿈
    while len(scoville) != 1 and scoville[0] < K:
        a, b = heapq.heappop(scoville), heapq.heappop(scoville) # scoville의 head를 팝
        scov = a + b*2
        heapq.heappush(scoville, scov) # scoville에 scov을 더 한다
        answer += 1

    if scoville[0] < K:
        return -1
    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))