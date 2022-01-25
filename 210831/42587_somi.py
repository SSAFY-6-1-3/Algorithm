def solution(properties, location):
    properties_q = list([index, prop] for index, prop in enumerate(properties))  # location을 알기 위해서 enumerate 사용
    count = 0 # 몇번 프린트 했는 지 세기
    while properties_q: # queue
        now = properties_q.pop(0) # 첫 번째 파일을 pop
        for i in range(len(properties_q)): # 나머지 파일과 비교해서
            if now[1] < properties_q[i][1]: # 우선순위가 낮다면
                properties_q.append(now)    # 맨 뒤로 보내주기
                break
        else: # 만약 모든 파일과 비교해서 우선순위가 낮지 않다면
            count += 1 # 프린트 해주기
            if now[0] == location: # 이때 프린트한 파일이 찾던 파일이라면
                return count       # 프린트 횟수 return


# 나와 비슷한 다른 사람의 풀이
# 다른 파일과 비교하는 부분(6 for ~ 9 break) any 사용가능!!!
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer