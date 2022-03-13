


N = int(input())

used = {N}
able = {N}
cnt = 0

while True:
    tmp = set()
    for n in able:
        if n == 1:
            print(cnt)
            exit()
        if not n%3 and n//3 not in used:
            tmp.add(n//3)
            used.add(n//3)
        if not n%2 and n//2 not in used:
            tmp.add(n//2)
            used.add(n//2)
        if n-1 not in used:
            tmp.add(n-1)
            used.add(n-1)

    cnt +=1
    able = tmp
