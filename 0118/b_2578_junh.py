
def check(r, c):
    if not sum(bingo[r]):
        garo[r] = 1

    sero_sum = 0
    for i in range(5):
        sero_sum += bingo[i][c]
    if not sero_sum:
        sero[c] = 1

    diagL = 0
    if r == c:
        for i in range(5):
            diagL += bingo[i][i]
        if not diagL:
            diag[0] = 1

    diagR = 0
    if r+c == 4:
        for i in range(5):
            diagR += bingo[i][4-i]
        if not diagR:
            diag[1] = 1

    if sum(garo) + sum(sero) + sum(diag) >= 3:
        return True
    return False



def solut(bingo, nums):
    for i in range(1, 26):
        num = nums[i]
        stop = False
        for r in range(5):
            for c in range(5):
                if bingo[r][c] == num:
                    stop = True
                    bingo[r][c] = 0
                    if check(r, c): # i>=12 가 아닌 경우?
                        return i
                    break
            if stop: break



bingo = [list(map(int, input().split())) for _ in range(5)]
nums = [None]
for _ in range(5):
    nums.extend(list(map(int, input().split())))

    garo = [0] * 5
    sero = [0] * 5
    diag = [0] * 2
print(solut(bingo, nums))