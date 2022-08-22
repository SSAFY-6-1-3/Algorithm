def solution(a):
    n = len(a)
    answer = n

    dp_l = [i for i in range(n)]
    dp_r = [i for i in range(n)]

    for i in range(1, n):
        if a[dp_l[i-1]] < a[dp_l[i]]:
            dp_l[i] = dp_l[i-1]

        if a[dp_r[n-i]] < a[dp_r[n-1-i]]:
            dp_r[n-i-1] = dp_r[n-i]


    for i in range(n):
        if a[i] > a[dp_l[i]] and a[i] > a[dp_r[i]]:
            answer -= 1


    return answer


print(solution([9, -1, -5]))
print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))