def solution(s):
    answer = len(s)
    for l in range(1, len(s)//2+1):                         # 1부터 len(s)//2+1까지 크기만큼 글자 끊어서 확인하기
        result = ''
        cnt = 0
        word_l = 0
        for start in range(0, len(s)-l+1, l):
            if s[start:start+l] == s[start+l:start+(2*l)]:  # 뒤의 글자와 지금 글자가 같은지 확인
                if result == s[start:start+l]:              # 이미 전에 같은 글자가 있는 경우
                    cnt += 1
                else:                                       # 이제 같은 글자가 나오기 시작한 경우 -> 같은 글자는 2개
                    result = s[start:start+l]               # 바로 전에 글자도 같은 글자였는지 확인하기위해 저장
                    cnt += 2
            else:                                           # 다른 글자가 나온 경우
                if cnt:                                     # 다른 글자가 나오기 시작 -> 그 전에 저장해놨던 같은 글자 갯수 더하기
                    word_l += len(str(cnt)) + l
                    cnt = 0                                 # 연속되는 글자 없어졌으므로 cnt = 0으로 초기화
                else:                                       # 그 전에도 연속되는 글자 계속 없었던 경우
                    word_l += l
        if cnt:                                             # 연속되는 글자로 끝나는 경우 더해주기
            word_l += len(str(cnt)) + l
        word_l += len(s) % l                                # 끊는 글자 단위로 나누어 떨어지지않을 때, 나머지 글자 더해주기
        answer = min(answer, word_l)
    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))


# 다른 사람 풀이
# def compress(text, tok_len):
#     words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
#     res = []
#     cur_word = words[0]
#     cur_cnt = 1
#     for a, b in zip(words, words[1:] + ['']):
#         if a == b:
#             cur_cnt += 1
#         else:
#             res.append([cur_word, cur_cnt])
#             cur_word = b
#             cur_cnt = 1
#     return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)
#
# def solution(text):
#     return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])