def pay(person, won):
    if won < 1:                                 # 현재 금액이 1원 이하일 때 이익을 나눌 필요 없으니까 바로 return
        return

    if people[person] == '-':                   # 최상단 바로 밑이면 저장해주고 return
        profit[person] += won - (won // 10)
        return

    profit[person] += won - (won // 10)
    pay(people[person], won // 10)


def solution(enroll, referral, seller, amount):
    for i in range(len(enroll)):                # 딕셔너리에 소개 받은 사람: 소개 시켜준 사람 형식으로 저장
        person = enroll[i]
        people[person] = referral[i]
        profit[person] = 0                      # 이익을 저장할 딕셔너리에 사람 이름 저장

    for j in range(len(seller)):                # seller에 있는 사람들 이익 구조 바로 계산
        pay(seller[j], amount[j] * 100)

    answer = []                                 # 딕셔너리 value로 리스트 만들기
    for e in enroll:
        answer.append(profit[e])
    return answer


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

people = {}
profit = {}
print(solution(enroll, referral, seller, amount))