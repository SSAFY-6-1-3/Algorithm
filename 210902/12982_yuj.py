d = [1,3,2,5,4]
budget = 9

len_d = len(d)

while sum(d) > budget:          # 부서가 신청한 합이 예산보다 작거나 같을 때까지
    d.remove(max(d))            # 가장 큰 값 리스트에서 지워버리기(작은 것들을 많이 차지)

len_d = len(d)
print(len_d)