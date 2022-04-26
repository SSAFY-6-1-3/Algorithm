text = str(input())
word = str(input())
w = len(word)
ans, idx = 0, 0
while idx != len(text):
    if word == text[idx:idx+w]:
        ans += 1
        idx += w
    else:
        idx += 1

print(ans)