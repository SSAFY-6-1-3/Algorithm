# 자릿수에 맞춰서 가중치 두기
# 1의 자리: 1, 10의 자리: 10, 100의 자리: 100...
# (숫자 위치, 빈도 둘 다 고려해야해서)
N = int(input())
dic = dict()
alpha = dict()
words = []
for _ in range(N):
    word = str(input())
    for i in range(len(word)):
        rev = len(word) - i - 1
        if word[i] in alpha:
            alpha[word[i]] += 10 ** rev
        else:
            alpha[word[i]] = 10 ** rev
    words.append(word)

# 가중치 제일 큰 값부터 9 -> 0 순으로 할당
number = 9
nums = sorted(set(alpha.values()), reverse=True)
for num in nums:
    keys = [key for key, value in alpha.items() if value == num]
    for k in keys:
        dic[k] = number
        number -= 1

ans = 0
for word in words:
    temp = ''
    for w in word:
        temp += str(dic[w])
    ans += int(temp)

print(ans)