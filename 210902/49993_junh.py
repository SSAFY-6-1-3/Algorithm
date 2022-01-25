def solution(skill, skill_trees):
    answer = 0 # 가능한 스킬 트리를 저장할 값

    for sk_tree in skill_trees: # 각 트리에서
        now_idx = -1 # 시작 idx는 -1
        for sk in sk_tree: # 트리의 각 스킬이
            if sk in skill: # skill 안에 주어져 있으면
                sk_idx = skill.find(sk)  # 그 순서(idx)를 기억한다.
                if not sk_idx == now_idx + 1: # 만약 그 idx가 현재 스킬 다음 idx가 아니면 브레이크
                    break
                else : # 다음 순서면 현재 스킬 idx +1
                    now_idx += 1
        else: # for문이 끝까지 돌았다면 가능한 스킬 트리임으로 ans +1
            answer += 1

    return answer



print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))