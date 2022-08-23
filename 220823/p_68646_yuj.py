# 원하는 곳을 기점으로 왼쪽 부분, 오른쪽 부분 나누기
# 왼쪽에서 제일 작은 수와 오른쪽에서 제일 작은 수 2개보다 모두 크면 실패
# 왼쪽, 오른쪽을 한 개의 수로 암축시킨다는 느낌
# 슬라이싱 + min 사용하니까 시간초과
def solution(a):
    answer = len(a)
    l, r = [0]*len(a), [0]*len(a)
    minl, minr = 1000000000, 1000000000
    for idx in range(len(a)):
        minl = min(minl, a[idx])
        minr = min(minr, a[answer-idx-1])
        l[idx] = minl
        r[answer-idx-1] = minr

    for j in range(len(a)):
        if a[j] > l[j] and a[j] > r[j]:
            answer -= 1
    return answer

print(solution([9,-1,-5]))
print(solution(	[-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))