'''
아직 못품
다른 풀이방법 생각해보기.
'''

def permutation(i, n):
    global operators_set, operators_list
    if i == n:
        operators_set.append(operators_list)
    else:
        for j in range(i, n):
            operators_list[i], operators_list[j] = operators_list[j], operators_list[i]
            permutation(i+1, n)
            operators_list[i], operators_list[j] = operators_list[j], operators_list[i]

N = int(input())
numbers = list(map(int, input().split()))
operators_count = list(map(int, input().split()))
operators = ['+', '-', '*', '//']
operators_list = []


for j in range(4):
    if operators_count[j]:
        operators_list.extend(operators[j] * operators_count[j])

n = len(operators_list)
operators_set = []
permutation(0, n)

print(operators_set)

# min_num = 1000000001
# max_num = -1000000001
answers = []
for operators in operators_set:
    n = numbers[0]
    for i in range(N-1):
        if operators[i] == '+':
            n += numbers[i + 1]
        elif operators[i] == '-':
            n -= numbers[i + 1]
        elif operators[i] == '*':
            n *= numbers[i + 1]
        elif operators[i] == '//':
            if numbers[i + 1] < 0:
                n = (- numbers[i + 1]) // n
            else:
                n //= numbers[i + 1]

    answers.append(n)

print(max(answers))
print(min(answers))





