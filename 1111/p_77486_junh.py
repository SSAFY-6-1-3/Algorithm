import sys
sys.setrecursionlimit(100000)

def solution(enroll, referral, seller, amount):
    N = len(enroll)
    answer = [0]*N
    dict = {}
    for i in range(N):
        dict[enroll[i]] = i

    def dfs(idx, money):

        to_rf = money//10
        money -= to_rf
        answer[idx] += money

        if not to_rf: return
        if referral[idx] =='-': return

        rf_idx = dict[referral[idx]]
        dfs(rf_idx, to_rf)

    for s in range(len(seller)):
        idx = dict[seller[s]]
        dfs(idx, amount[s]*100)

    return answer


print(
    solution(
        ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
        ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
        ["young", "john", "tod", "emily", "mary"],
        [12, 4, 2, 5, 10],
    )
)