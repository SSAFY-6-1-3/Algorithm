def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        line = ""
        a, b = arr1[i], arr2[i]
        a_bin = str(bin(a))[2:].zfill(n)
        b_bin = str(bin(b))[2:].zfill(n)

        for j in range(n):
            if a_bin[j] == '1' or b_bin[j] == '1':
                line += "#"
            else:
                line += " "

        answer.append(line)

    return answer



print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))