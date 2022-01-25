
def make_dic(nums):
    dic = {}
    for num in nums:
        if dic.get(num):
            dic[num] += 1
        else:
            dic[num] = 1
    return dic

def answer(nums, dic):
    answer = []
    for num in nums:
        if dic.get(num):
            answer.append(dic[num])
        else:
            answer.append(0)
    return answer

N = int(input())
nums = map(int, input().split())

dic = make_dic(nums)

M = int(input())
mums = map(int, input().split())

print(*answer(mums, dic))