def solution(lottos, win_nums):
    lotto_num = 0
    zero = 0
    for lotto in lottos:
        if lotto in win_nums:
            lotto_num += 1
        elif lotto == 0:
            zero += 1

    if lotto_num:
        answer = [7-lotto_num-zero, 7-lotto_num]
    elif zero:
        answer = [7 - zero, 6]
    else:
        answer = [6, 6]
    return answer

lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
print(solution(lottos, win_nums))
