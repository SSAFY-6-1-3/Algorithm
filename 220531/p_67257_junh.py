
def calcul(left, right, calc):
    if calc == '+':
        return left + right
    if calc == '-':
        return left - right
    return left * right

orders = []
def rules(calcs):
    if len(calcs) == 3:
        orders.append(calcs)
        return

    for c in '+-*':
        if c in calcs: continue
        rules(calcs + c)

rules('')

def solution(expression):
    answer = 0
    li = []
    tmp = ''
    for i in range(len(expression)):
        if expression[i] in '+-*':
            li.append(int(tmp))
            li.append(expression[i])
            tmp = ''
        else:
            tmp += expression[i]
    li.append(int(tmp))


    for order in orders:
        exp = li[:]

        for calc in order:
            i = 0
            while i<len(exp):
                if exp[i] == calc:
                    rst = calcul(exp[i-1], exp[i+1], calc)
                    if i+2 < len(exp):
                        exp = exp[:i-1] + [rst] + exp[i+2:]
                    else:
                        exp = exp[:i-1] + [rst]
                    i = i-1
                else:
                    i += 1
        answer = max(answer, abs(int(exp[0])))

    return answer


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))