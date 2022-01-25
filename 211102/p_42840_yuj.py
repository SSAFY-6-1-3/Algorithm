answers = [1,2,3,4,5]

a = [1, 2, 3, 4, 5]
b = [2, 1, 2, 3, 2, 4, 2, 5]
c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
cnt = [0] * 4

for idx in range(len(answers)):
    answer = answers[idx]
    if answer == a[idx % 5]:
        cnt[1] += 1
    if answer == b[idx % 8]:
        cnt[2] += 1
    if answer == c[idx % 10]:
        cnt[3] += 1

maxv = max(cnt)
result = []
for i in range(1, 4):
    if maxv == cnt[i]:
        result.append(i)

print(result)