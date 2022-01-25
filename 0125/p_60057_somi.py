def solution(s):
    answer = 1000
    for i in range(1, len(s) + 1):  # 몇개 단위로 자를 지
        tmp = ""            # 압축 문자

        pattern = s[: i]
        cnt = 1
        for j in range(i, len(s) + i, i):
            if pattern == s[j: j + i]:
               cnt += 1
            else:
                if cnt > 1:
                    tmp += str(cnt) + str(pattern)
                else:
                    tmp += str(pattern)

                pattern = s[j: j + i]
                cnt = 1
        answer = min(answer, len(tmp))
    return answer


print(solution("aabbaccc"))