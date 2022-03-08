def solution(s):
    answer = []
    s = s.lstrip('{').rstrip('}').split('},{')

    dict = {}

    for st in s:
        for n in st.split(','):
            if dict.get(n):
                dict[n] += 1
            else:
                dict[n] = 1
    for n, _ in sorted(dict.items(), key=lambda x:-x[1]):
        answer.append(int(n))


    return answer



print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))