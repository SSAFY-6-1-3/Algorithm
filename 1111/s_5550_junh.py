import sys
sys.stdin = open('s_5550.txt')

def frog(st):
    checked = set()
    idx = 0
    frogs = 0
    while True:
        crocked = False
        frogs +=1
        for c in range(len(st)):
            if c in checked: continue
            if "croak"[idx] != st[c]: continue
            checked.add(c)
            idx += 1
            if idx==5:
                idx=0
                crocked=True
        if not crocked or idx:
            return -1
        if len(checked) == len(st):
            return frogs




T = int(input())
for tc in range(1, T+1):
    st = input()
    print('#{} {}'.format(tc, frog(st)))