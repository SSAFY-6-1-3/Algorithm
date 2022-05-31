from itertools import permutations

def make_formula(expression):
    formula = []
    operators = set()
    num = ''
    for e in expression:
        if e.isdigit():
            num += e
        else:
            formula.append(num)
            num = ''
            formula.append(e)
            operators.add(e)
    formula.append(num)
    return formula, list(operators)

def calculate(op, num1, num2):
    if op == "+":
        return int(num1) + int(num2)
    elif op == "*":
        return int(num1) * int(num2)
    else:
        return int(num1) - int(num2)

def calculator(form, cal):
    for op in cal:
        stack = []
        while form:
            temp = form.pop(0)
            if temp == op:
                stack.append(calculate(temp, stack.pop(), form.pop(0)))
            else:
                stack.append(temp)
        form.extend(stack)
    return abs(form[0])



def solution(expression):
    answer = 0
    formula, operators = make_formula(expression)
    cals = list(permutations(operators, len(operators)))
    for cal in cals:
        answer = max(answer, calculator(formula[:], cal))
    return answer


print(solution("50*6-3*2"))