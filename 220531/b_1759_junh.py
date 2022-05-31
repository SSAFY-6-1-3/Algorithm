
L, C = map(int, input().split())
moems = 'aeiou'

chars = input().split()
chars.sort()

answer = []

def make(pw, idx, j, m):
    if len(pw) == L and j>1 and m:
        answer.append(pw)
        return

    for i in range(idx, C):
        c = chars[i]

        if c in moems:
            make(pw+c, i+1, j, m+1)
        else:
            make(pw+c, i+1, j+1, m)


make('', 0, 0, 0)

for a in answer:
    print(a)