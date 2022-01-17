import sys

sys.stdin = open('s_4047_input.txt')

def solut(cards):
    dic = {
        'S': [0] * 14,
        'D': [0] * 14,
        'H': [0] * 14,
        'C': [0] * 14,
    }

    for i in range(0, len(cards), 3):
        if dic[cards[i]][int(cards[i+1:i+3])]:
            return 'ERROR'
        else:
            dic[cards[i]][int(cards[i+1:i+3])] = 1

    answer = [13] * 4
    answer[0] -= sum(dic['S'])
    answer[1] -= sum(dic['D'])
    answer[2] -= sum(dic['H'])
    answer[3] -= sum(dic['C'])
    answer = list(map(str, answer))

    return ' '.join(answer)


T = int(input())
for tc in range(1, T+1):
    cards = input()

    print('#{} {}'.format(tc, solut(cards)))