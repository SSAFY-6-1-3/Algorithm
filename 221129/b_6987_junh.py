matches = []

def make_matches(team):
    if team == 6:
        return
    for i in range(team + 1, 6):
        matches.append([team, i])
    make_matches(team + 1)


make_matches(0)
results = []

def make_results(idx):
    global found

    a, b = matches[idx]
    for i in range(3):
        ai = 3*a + i
        bi = 3*b + (2-i)
        if not result[ai] or not result[bi]:
            continue
        result[ai] -= 1
        result[bi] -= 1
        if idx == 14:
            if sum(result) == 0:
                found = 1
        else:
            make_results(idx+1)
        if found: return
        result[ai] += 1
        result[bi] += 1


answer = ''
for _ in range(4):
    result = list(map(int, input().split()))
    found = 0
    make_results(0)
    answer += str(found) + ' '

print(answer)

