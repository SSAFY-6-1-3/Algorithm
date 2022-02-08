def binary(arr, n):
    new = []
    for num in arr:
        bin_num = ''
        while num:
            bin_num += str(num % 2)
            num //= 2
        while len(bin_num) < n:
            bin_num += '0'
        new.append(bin_num[::-1])

    return new

def solution(n, arr1, arr2):
    answer = []
    new_arr1 = binary(arr1, n)
    new_arr2 = binary(arr2, n)
    for r in range(n):
        temp = ''
        for c in range(n):
            if int(new_arr1[r][c]) | int(new_arr2[r][c]):
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))