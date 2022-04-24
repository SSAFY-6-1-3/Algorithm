st = input()
kw = input()

def st_check(idx, kw):
    if idx+len(kw) > len(st):
        return False
    if st[idx:idx+len(kw)] == kw:
        return True
    return False

i = 0
cnt = 0
while i < len(st):
    if st_check(i, kw):
        i += len(kw)
        cnt += 1
    else:
        i += 1

print(cnt)