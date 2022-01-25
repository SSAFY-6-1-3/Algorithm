def solution(priorities, location):
    answer = 0
    while priorities:
        j = priorities.pop(0)
        for p in priorities:
            if p > j:
                priorities.append(j)
                location -= 1
                if location < 0:
                    location = len(priorities)-1
                break

    return answer