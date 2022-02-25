def solution(files):
    hnts = []
    for i in range(len(files)):
        file = files[i]
        hnt = ['', 0, i, file]

        n_start = 0
        for j in range(len(file)):
            c = file[j]
            if not '0' <= c <= '9':         # 65 ~ 122
                hnt[0] += c.lower()
            else:
                n_start = j
                break

        num = ''
        for n in range(n_start, len(file)):
            c = file[n]
            if '0' <= c <= '9':
                num += c
            else:
                break
        hnt[1] = int(num)

        hnts.append(hnt)

    hnts.sort()
    answer = [hnt[3] for hnt in hnts]

    return answer



print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))