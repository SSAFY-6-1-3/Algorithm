def solution(people, limit):
    answer = 0
    people.sort(reverse=True)

    s, e = 0, len(people)-1

    while s<=e:
        if people[s] + people[e] <= limit:
            s += 1
            e -= 1
        else:
            s += 1
        answer += 1

    return answer



    # people.sort(reverse=True)
    # boats = []
    # answer = 0
    #
    # for p in people:
    #     for b in range(len(boats)):
    #         if boats[b] + p <= limit:
    #             boats.pop(b)
    #             answer += 1
    #             break
    #     else:
    #         boats.append(p)
    #
    #
    #
    # return len(boats) + answer



print(solution([70, 50, 80, 50], 100))