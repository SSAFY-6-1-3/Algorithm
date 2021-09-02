def solution(priorities, location):  # 원형큐 이용
    print_lst = [(-1, -1)]
    front, rear = 0, -1
    mod = len(priorities) + 1
    new_text = list(enumerate(priorities+[0]))
    answer = 0
    while print_lst[-1][0] != location:  # 현재 인쇄된 목록 마지막에 우리가 찾는 문서가 있을때까지 반복
        temp = (front + 1) % mod  # 우선순위를 비교할 문서를 찾기 위한 변수
        plus_print = True  # 인쇄목록에 추가할지 여부를 판단하게 해주는 변수

        while temp != front:
            if new_text[front][1] < new_text[temp][1]:
                new_text[rear] = new_text[front]
                new_text[front] = (-1, -1)
                front = (front + 1) % mod
                rear = (rear + 1) % mod
                plus_print = False
                break
            temp = (temp + 1) % mod

        if plus_print:
            print_lst.append(new_text[front])
            new_text[front] = (-1, -1)
            answer += 1

    return answer