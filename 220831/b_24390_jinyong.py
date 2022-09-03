M, S = map(int, input().split(":"))
t = M * 60 + S


def solution(time):
    answer = 0

    answer += time // 600
    time = time % 600

    answer += time // 60
    time = time % 60

    if time >= 30:  # 남아있는 시간이 30초 이상인 경우
        # 전자레인지를 동작하면서 30초를 얻는 것이 이득이 된다
        # 따라서 30으로 나눈 몫만큼 연속으로 시작 버튼을 누른다고 생각하자
        answer += time // 30
        time = time % 30
        answer += time // 10

    else:  # 남아있는 시간이 30초 미만인 경우
        # 10초를 최대 2번 누르게 된다는 의미이므로
        # 시작 버튼은 시간을 모두 추가한 뒤 눌러도 된다
        answer += time // 10
        answer += 1

    return answer


print(solution(t))
