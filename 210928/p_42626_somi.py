'''
더 맵게
min heap....??

런타임에러 ㅠㅠ
'''


# def selection_sort(scoville):
#     for i in range(2):
#         min_index = i
#         for j in range(i+1, len(scoville)):
#             if scoville[i] > scoville[j]:
#                 min_index = j
#         scoville[i], scoville[min_index] = scoville[min_index], scoville[i]
#     return scoville

def solution(scoville, K):

    count = -1
    while True:
        # selection_sort(scoville)  # 선택정렬이 더 오래걸림
        scoville.sort()         # 일단 정렬
        if scoville[0] < K:     # 가장 작은 값이 K보다 작으면
            a = scoville.pop(0)
            b = scoville.pop(0)
            scoville.append(a + (b * 2))  # 음식 섞기
            count += 1

        else:  # 모든 음식의 지수가 K이상이면
            return count + 1  # count 리턴



print(solution([1, 2, 3, 9, 10, 12], 7))


