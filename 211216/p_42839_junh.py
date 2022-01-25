def get_primes(num):
    primes = []
    for i in range(2, int(num ** 0.5) + 1):
        divided = False
        for p in primes:
            if not i % p:
                divided = True
                break
        if not divided:
            primes.append(i)
    return primes



def solution(numbers):
    largest = int(''.join(sorted(numbers, reverse=True)))
    primes = get_primes(largest)
    answer = 0
    nums = set()

    def get_num(result, depth, numbers_list):
        nonlocal nums
        if not depth:
            return
        for i in range(len(numbers_list)):
            nums.add(int(result+numbers_list[i]))
            get_num(result + numbers_list[i], depth - 1, numbers_list[:i]+numbers_list[i+1:])

    get_num('', len(numbers), list(numbers))

    for num in nums:
        if num <= 1: continue
        for prime in primes:
            if num!=prime and not num%prime:
                break
        else:
            answer+=1

    return answer


print(solution("17"))
print(solution("011"))