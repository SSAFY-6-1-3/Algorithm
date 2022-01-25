
'''
sol1. 순열로 배열한뒤, 가장 큰 수를 리턴하기 => 런타임에러

def solution(numbers): # 순열로 배열한 수를 저장하고, 저장된 수 중 가장 큰 수를 반환하기
    global numbers_list

    numbers_list = []
    N = len(numbers)
    permutation(0, N, numbers)

    return str(max(numbers_list))

def permutation(i, N, numbers): # 순열 구하는 함수
    global numbers_list

    if i == N:
        numbers_list.append(int(''.join(map(str, numbers))))

    else:
        for j in range(i, N):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            permutation(i+1, N, numbers)
            numbers[i], numbers[j] = numbers[j], numbers[i]

print(solution([3, 30, 34, 5, 9]))

'''''


'''
sol2. 숫자 -> str 변환후, 3번 반복하여 정렬

numbers = ['999', '333', '303030', '343434', '555']
print(sorted(numbers))
['303030', '333', '343434', '555', '999']
'''


def solution(numbers):
    numbers_thrice = sorted([(str(num) * 3, str(num)) for num in numbers], key= lambda x : x[0], reverse= True)
    answer = ''
    for number in numbers_thrice:
        answer += number[1]

    # 모두 0인 경우도 고려 필요(test 11)
    if answer[0] == '0':
        return '0'

    return answer

numbers = [0, 0, 0, 0]
# numbers = ['9', '3', '30', '34', '5']
print(solution(numbers))