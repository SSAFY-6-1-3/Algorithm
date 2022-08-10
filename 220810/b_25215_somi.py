word = input()
ans = len(word)
is_diamond = False  # 소문자로 시작

upper_word = [False] * len(word)
for i in range(len(word)):
    if word[i].isupper():
        upper_word[i] = True

idx = 0
while idx < len(word):
    if upper_word[idx] != is_diamond:  # 변환 필요
        if idx == len(word) - 1 or upper_word[idx] != upper_word[idx + 1]:  # star
            ans += 1
            idx += 1
        else:  # diamond
            ans += 1
            is_diamond = not is_diamond
            idx += 1
    idx += 1

print(ans)
