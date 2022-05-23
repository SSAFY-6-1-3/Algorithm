document = input()  # 문서
word = input()      # 찾을 단어
cnt = 0             # 등장 횟수
i = 0               # 인덱스
while i <= len(document):
    if document[i:i + len(word)] == word:
        cnt += 1
        i += len(word)
    else:
        i += 1

print(cnt)