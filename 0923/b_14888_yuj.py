import sys
from itertools import permutations
sys.stdin = open('input.txt')

def calculate(num_lst, op_lst):
    operators = ['+', '-', '*', '/']
    operator = []
    for i in range(4):
        for j in range(op_lst[i]):
            operator.append(operators[i])

    op = list(set(permutations(operator, N-1)))         # 연산자 순열 이용해서 모든 경우 구하기(set 안 쓰면 시간 초과)
    results = []
    for k in range(len(op)):
        result = num_lst[0]
        for l in range(N-1):
            if op[k][l-1] == '+':
                result += num_lst[l+1]
            elif op[k][l-1] == '*':
                result *= num_lst[l+1]
            elif op[k][l-1] == '-':
                result -= num_lst[l+1]
            elif op[k][l-1] == '/':
                if result < 0:
                    result = -(abs(result) // num_lst[l+1])
                else:
                    result //= num_lst[l+1]
        results.append(result)

    return [max(results), min(results)]



N = int(input())
num_lst = list(map(int,input().split()))
op_lst = list(map(int,input().split()))
sorted(num_lst)
print(calculate(num_lst, op_lst)[0])
print(calculate(num_lst, op_lst)[1])