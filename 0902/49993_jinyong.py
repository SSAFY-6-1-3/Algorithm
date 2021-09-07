def solution(skill, skill_trees):
    learn_skill = []
    idx = 0
    answer = 0
    skill = list(skill)
    for skill_ele in skill_trees:
        learn_skill.clear()
        idx = 0
        for sk in skill_ele:
            if sk not in skill:
                continue

            learn_skill.append(sk)
            idx += 1
            if learn_skill[:idx] != skill[:idx]:
                break

        else:
            answer += 1

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
