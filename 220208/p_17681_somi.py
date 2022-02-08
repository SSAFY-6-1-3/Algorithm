def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        map1 = bin(arr1[i])[2:].zfill(n)  #  n만큼 길이 맞춰주기
        map2 = bin(arr2[i])[2:].zfill(n)
        tmp = ""
        for j in range(n):
            if map1[j] == "1" or map2[j] == "1":   # 둘 중 하나만 벽이어도 전체 지도에는 벽
                tmp += "#"
            else:
                tmp += " "
        answer.append(tmp)
    return answer


print(solution(5, [9, 20, 28, 18, 11],[30, 1, 21, 17, 28] ))
