
def solution(answers):
    spj = [0, 0, 0]

    for i in range(len(answers)):
        ans = answers[i]

        if i%5 +1 == ans:
            spj[0] +=1

        for1 = [1, 3, 4, 5]
        if i%2 == 0 and ans == 2:
            spj[1] += 1
        elif i%2 == 1 and for1[i//2 % 4] == ans:
            spj[1] += 1

        for2 = [3, 1, 2, 4, 5]
        if for2[i%10//2] == ans:
            spj[2] +=1

    rtn = []
    max_pnt = max(spj)
    for i in range(3):
        if spj[i] == max_pnt:
            rtn.append(i+1)
    return rtn

print(solution([1,3,2,4,2]))

