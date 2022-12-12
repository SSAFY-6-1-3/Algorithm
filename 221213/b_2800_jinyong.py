formula = input()
n = len(formula)
answer = set()


def solution(idx, result, stack):

    if idx == n:
        if result != formula:
            answer.add(result)
        return

    if formula[idx] == "(":
        solution(idx + 1, result + "(", stack + [0])
        solution(idx + 1, result, stack + [1])

    elif formula[idx] == ")":
        is_correct = stack.pop()

        if is_correct:
            solution(idx + 1, result, stack)
        else:
            solution(idx + 1, result + ")", stack)

    else:
        solution(idx + 1, result + formula[idx], stack)


solution(0, "", [])

ans_lst = sorted(list(answer))
for ans in ans_lst:
    print(ans)
