def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        r = i // n
        c = i % n
        answer.append(max(r, c) + 1)
    return answer

'''
 시간초과
def solution(n, left, right):

    arr = [0 for _ in range(n * n)]
    now = 0
    while now < right:
        for i in range(1, n + 1):
            for j in range(i):
                arr[now] = i
                now += 1
            for k in range(i + 1, n + 1):
                arr[now] = k
                now += 1
    return arr[left:right + 1]
'''




solution(4, 7, 14)