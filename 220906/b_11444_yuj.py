# n번째 피보나치수 = (행렬[[1, 1], [1, 0]] * n)의 (0, 1) 수
import sys
input = sys.stdin.readline

def mul(m1, m2):                # 행렬 계산 함수
    result = []
    for i in range(2):
        temp = []
        for j in range(2):
            temp_num = 0
            for k in range(2):
                temp_num += m1[i][k] * m2[k][j]
            temp.append(temp_num % 1000000007)
        result.append(temp)

    return result

def cal(n):                     # 분할 정복 함수
    global matrix

    if n == 1:
        return matrix

    temp_m = cal(n//2)
    if not n % 2:
        return mul(temp_m, temp_m)
    else:
        return mul(mul(temp_m, temp_m), matrix)

num = int(input())
matrix = [[1, 1], [1, 0]]
print(cal(num)[0][1])