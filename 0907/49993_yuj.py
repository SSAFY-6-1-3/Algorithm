skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
cnt = 0

for i in range(len(skill_trees)):           # skill_trees에서 하나씩 비교
    word = ''
    for alpha in skill_trees[i]:
        if alpha in skill:
            word += alpha

    if not word:                            # 아예 skill알파벳이 안 들어간 경우
        cnt += 1
        continue

    if skill[0] != word[0]:                 # skill의 첫번째 알파벳이 맨 처음에 있지 않은 경우는 애초에 불가능한 스킬트리
        continue

    if word in skill:
        cnt += 1

print(cnt)

