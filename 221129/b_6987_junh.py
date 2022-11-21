from copy import deepcopy

matches = []

def make_matches(team):
    if team == 6:
        return
    for i in range(team + 1, 6):
        matches.append([team, i])
    make_matches(team + 1)

make_matches(0)
print(matches)
results = []


def make_results(idx, result = [0] * 18):
    if idx == 3:
        results.append(result)
        return

    a, b = matches[idx]
    a *= 3
    b *= 3

    result[a] += 1
    result[b+2] += 1
    make_results(idx+1, deepcopy(result))
    result[a] -= 1
    result[b+2] -= 1

    result[a+1] += 1
    result[b+1] += 1
    make_results(idx+1, deepcopy(result))
    result[a+1] -= 1
    result[b+1] -= 1

    result[a+2] += 1
    result[b] += 1
    make_results(idx+1, deepcopy(result))
    result[a+2] -= 1
    result[b] -= 1


make_results(0)
print(results)