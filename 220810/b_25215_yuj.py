words = str(input())
up = 0
cnt = len(words)
for idx in range(len(words)):
    if words[idx].isupper():
        if not up:
            if idx < len(words)-1 and words[idx+1].isupper():
                up = 1
            cnt += 1
    else:
        if up:
            if idx < len(words)-1 and not words[idx+1].isupper():
                up = 0
            cnt += 1
print(cnt)