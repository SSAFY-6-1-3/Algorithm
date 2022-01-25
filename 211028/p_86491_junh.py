def solution(sizes):
    sh, lg = 0, 0
    for s, l in sizes:
        if s>l:
            s, l = l, s
        sh = max(sh, s)
        lg = max(lg, l)

    return sh*lg