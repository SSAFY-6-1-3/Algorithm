def solution(n, lost, reserve):
    temp = [0] + [1] * n

    for i in lost:
        temp[i] -= 1

    for i in reserve:
        temp[i] += 1

    for i in range(n+1):
        if temp[i] <= 1:
            continue

        if i-1 >= 1 and not temp[i-1]:
            temp[i-1] += 1
            temp[i] -= 1
            continue

        if i+1 <= n and not temp[i+1]:
            temp[i+1] += 1
            temp[i] -= 1

    return (n+1) - temp.count(0)


print(solution(10, [2, 3, 4], [1, 3, 5]))
print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
