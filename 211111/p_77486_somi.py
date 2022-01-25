def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    enroll_dict = {}
    for j in range(len(enroll)):
        enroll_dict[enroll[j]] = [j, referral[j]]
    print(enroll_dict)

    for i in range(len(seller)):

        profit = amount[i] * 100
        sel = seller[i]
        ref = enroll_dict[seller[i]][1]

        while profit and ref != '-':


            sel_profit = profit if (profit // 10) < 1 else (profit - (profit // 10))
            answer[enroll_dict[sel][0]] += sel_profit
            profit -= sel_profit
            sel = ref
            ref = enroll_dict[sel][1]


        answer[enroll_dict[sel][0]] += (profit - profit // 10)

    return answer

'''
index 쓰면 4문제 시간초과
def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)

    for i in range(len(seller)):
        seller_index = enroll.index(seller[i])
        profit = amount[i] * 100

        ref = referral[seller_index]
        sel = seller[i]
        while profit and ref != '-':
            ref_index = enroll.index(ref)
            sel_index = enroll.index(sel)
            sel_profit = profit if (profit // 10) < 1 else (profit - profit // 10)
            answer[sel_index] += sel_profit
            profit -= sel_profit
            sel = ref
            ref = referral[ref_index]


        answer[enroll.index(sel)] += (profit - profit // 10)
    return answer
'''

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))

