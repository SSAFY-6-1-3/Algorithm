import sys
sys.stdin=open('input.txt')

def snow(ball, now, M):
    global result

    if now >= N or M == 0:          # 남아있는 시간이 0이거나/ 현재 위치가 마지막 위치보다 클 때
        result.append(ball)         # 마지막 눈덩이 리스트에 추가하기
        return

    if now <= N-1:                          # 남은 거리 확인 후 눈덩이 굴리기
        snow(ball+lst[now+1], now+1, M-1)
    if now <= N-2:                          # 남은 거리 확인 후 눈덩이 던지기
        snow(ball//2+lst[now+2], now+2,M-1)

N, M = map(int,input().split())
lst = [0] + list(map(int,input().split()))  # 인덱스 맞추기 위해서 0 추가
result = []             # 나올 수 있는 눈덩이 저장

snow(1, 0, M)
print(max(result))      # 만들어진 눈덩이 중에 가장 큰 눈덩이 출력
