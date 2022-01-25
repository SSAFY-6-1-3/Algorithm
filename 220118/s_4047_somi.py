import sys
sys.stdin=open('s_4047_input.txt')

T = int(input())
for tc in range(1, T + 1):
    print('#', tc, sep='', end=' ')
    cards = {
        'S': [],
        'D': [],
        'H': [],
        'C': [],
    }

    now = input()
    flag = False
    for i in range(0, len(now) - 2, 3):
        T, xy = now[i], now[i + 1: i + 3]
        if xy in cards[T]:
            flag = True
            break
        cards[T].append(xy)
    if flag:
        print('ERROR')
        continue
    else:
        for card in cards:
            print(13-len(cards[card]), end=' ')
    print()
        # print(13 - len(cards['S']), 13 - len(cards['D']), 13-len(cards['H']), 13-len(cards['C']))

