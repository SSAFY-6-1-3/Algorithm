'''
삼각 달팽이
'''

def solution(n):

    triangle = []
    for i in range(1, n + 1):  # 0으로 채워진 삼각형 모양 2차원 리스트 생성
        sub_list = [0] * i
        triangle.append(sub_list)

    direction = [[1, 0], [0, 1], [-1, -1]]  # 반시계 방향으로 움직이기

    length = n  # 한 방향으로 이동할 길이
    di = 0  # direction 인덱스
    r, c = -1, 0  # 숫자 넣을 위치
    number = 0  # 채울 숫자

    while length > 0:  # 이동할 길이가 0보다 클 때

        for _ in range(length):  # 한 방향으로 for문을 돌면서 숫자 채워넣기
            number += 1  # 채울 숫자를 1씩 증가
            r += direction[di][0]  # 숫자 넣을 인덱스
            c += direction[di][1]
            triangle[r][c] = number  # 숫자 저장하기

        length -= 1  # 이동할 길이가 1씩 줄어듬
        di = (di + 1) % 3  # 그 다음 이동할 방향

    answer = []
    for i in triangle: # 2중 리스트 풀어주기
        answer.extend(i)
    return answer

print(solution(6))

