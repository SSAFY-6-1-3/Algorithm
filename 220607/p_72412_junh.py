from collections import deque

def solution(info, query):
    answer = []
    dict = {}

    def put_code(code, score):
        q = [code]
        idx = 0

        while idx < len(q):
            cd = q[idx]
            idx += 1

            dict[cd] = dict.get(cd, []) + [score]

            for i in range(4):
                if cd[i] == '-': continue
                n_cd = cd[:i] + '-' + cd[i+1:]
                if n_cd in q: continue
                q.append(n_cd)


    for i in range(len(info)):
        info[i] = info[i].split()
        code = ''
        for c in range(4):
            code += info[i][c][0]
        put_code(code, int(info[i][4]))

    for key in dict.keys():
        dict[key] = sorted(dict[key], reverse=True)

    code_ch = ['jcp', 'bf', 'js', 'cp']

    def check(qr):
        code = ''
        for c in range(4):
            code += qr[c][0]
        std = qr[4]

        scores = dict.get(code, [])
        cnt = 0
        for i in range(len(scores)):
            if scores[i] >= std:
                cnt += 1
                continue
            break
        return cnt



    for qr in query:
        qr = qr.split('and')
        for j in range(len(qr)):
            qr[j] = qr[j].strip()
        a, b = qr[-1].split()
        qr[-1] = a
        qr.append(int(b))

        answer.append(check(qr))


    return answer



print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))