def solution(numbers, hand):
    left_now = (3, 0)
    right_now = (3, 2)

    left_nums = [1, 4, 7]
    right_nums = [3, 6, 9]
    mid_nums = [2, 5, 8, 0]

    answer = ''
    for number in numbers:
        if number in left_nums:
            answer += 'L'
            left_now = (left_nums.index(number), 0)


        elif number in right_nums:
            answer += 'R'
            right_now = (right_nums.index(number), 2)


        else:
            target = mid_nums.index(number)
            dist_l = abs(left_now[0] - target) + abs(left_now[1] - 1)

            dist_r = abs(right_now[0] - target) + abs(right_now[1] - 1)
            if dist_l < dist_r or (dist_l == dist_r and hand == 'left'):
                answer += 'L'
                left_now = (target, 1)


            elif dist_r < dist_l or (dist_l == dist_r and hand == 'right'):
                answer += 'R'
                right_now = (target, 1)



    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],  'right')

phone = [[1, 4, 7], [2, 5, 8, 0], [3, 6, 9]]