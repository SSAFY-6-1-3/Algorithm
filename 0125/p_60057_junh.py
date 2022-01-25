def solution(s):
    answer = 0

    for l in range(2, len(s)//2+1):
        st = ''
        idx = 0
        while idx <= len(s)-l:
            rep = s[idx:idx+l]
            rep_n = 0
            while s[idx + l+1 : idx + 2*l] == rep:
                idx += l

    return answer


