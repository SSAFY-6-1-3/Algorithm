import sys
sys.stdin=open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=" ")
    S = set()
    D = set()
    H = set()
    C = set()
    cards = str(input())

    for idx in range(0, len(cards), 3):
        num = int(cards[idx+1]+cards[idx+2])
        if cards[idx] == 'S':
            S.add(num)
        elif cards[idx] == 'D':
            D.add(num)
        elif cards[idx] == 'H':
            H.add(num)
        elif cards[idx] == 'C':
            C.add(num)

    zeros = [13-len(S), 13-len(D), 13-len(H), 13-len(C)]
    if sum(zeros) != 52-(len(cards)//3):
        print('ERROR')
    else:
        print(*zeros)
