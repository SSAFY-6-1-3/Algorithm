def solution(files):
    answer = []

    for file in files:
        start = 0  # 숫자 시작 인덱스
        cnt = 0    # 숫자 몇개인지
        for i in range(len(file)):
            if file[i].isdecimal():
                cnt += 1
                if not start:
                    start = i
            else:     # 이 부분 없으면 시간 초과
                if start:
                    break
        head = file[:start]
        number = file[start:start + cnt]
        answer.append([file, head, number])
    answer.sort(key=lambda x: (x[1].lower(), int(x[2])))
    return [ans[0] for ans in answer]


solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
solution( ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])