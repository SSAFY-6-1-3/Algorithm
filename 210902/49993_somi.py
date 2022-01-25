''''
skill trees
'''

def solution(skill, skill_trees):
    answer = 0  # 선행 스킬 순서를 지킨 트리 개수 세기
    for i in range(len(skill_trees)):
        index = 0  # skill 의 인덱스 (0부터 순서대로 증가)
        for j in range(len(skill_trees[i])):  # 스킬트리 스킬 순서 순환
            if skill_trees[i][j] in skill:    # 만약 해당 스킬이 선행 스킬인 경우,
                if skill_trees[i][j] != skill[index]:
                    break
                else:
                    index += 1
        else:
            answer += 1
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA", "CDBA"]))



# 다른사람의 풀이
# 스킬트리 중에서 선행 스킬만 따로 빼서 비교하는 방법!!

def solution(skill,skill_tree):
    answer=0
    for i in skill_tree:
        skillist=''  # 스킬 트리에서 skill에 해당하는 스킬만 담을 str
        for z in i:
            if z in skill:
                skillist+=z
        if skillist==skill[0:len(skillist)]: # 순서가 완전 동일해야 함
            answer+=1
    return answer