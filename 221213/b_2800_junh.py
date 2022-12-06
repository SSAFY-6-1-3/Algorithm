st = input()
gwalhos = []
stack = []
idx = -1
for i in range(len(st)):
    if st[i] == '(':
        stack.append(i)
    elif st[i] == ')':
        gwalhos.append((stack.pop(), i))

answers = []


def make_ans(comb):
    answer = ""
    excepts = set()
    for c in comb:
        excepts.update(gwalhos[c])

    for i in range(len(st)):
        if i not in excepts:
            answer += st[i]
    if answer not in answers:   # 동일한 답 처리
        answers.append(answer)


def combi(idx, comb):
    for i in range(idx+1, len(gwalhos)):
        make_ans(comb + [i])
        combi(i, comb + [i])


combi(-1, [])
answers.sort()

for ans in answers:
    print(ans)
