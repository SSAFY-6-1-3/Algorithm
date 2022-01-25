N = int(input())
num = list(float(input()) for _ in range(N))
results = [*num]

for i in range(N):
    tmp = num[i]
    result = [num[i]]
    for j in range(i + 1, N):
        tmp = tmp * num[j]
        if num[j] < tmp:
            result.append(tmp)
        else:
            break

    results.append(max(result))
ans = max(results)
print("{:.3f}".format(ans))

