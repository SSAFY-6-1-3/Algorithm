
N = int(input())

vid = [input() for _ in range(N)]

def is_same(zone):
    stnd = zone[0][0]
    for i in range(len(zone)):
        for j in range(len(zone[0])):
            if zone[i][j] != stnd:
                return False
    return stnd

def quad(zone, n):
    size = n//2
    if not size:
        return zone[0][0]
    divided = [
        [zone[i][:size] for i in range(size)],
        [zone[i][size:size*2] for i in range(size)],
        [zone[size+i][:size] for i in range(size)],
        [zone[size+i][size:size*2] for i in range(size)]
    ]
    rtn = ''

    for i in range(4):
        d = divided[i]
        d_res = is_same(d)
        if d_res:
            rtn += d_res
        else:
            rtn += quad(d, size)

    stnd = rtn[0]
    for c in rtn:
        if c != stnd:
            return '(' + rtn + ')'
    return stnd

print(quad(vid, N))