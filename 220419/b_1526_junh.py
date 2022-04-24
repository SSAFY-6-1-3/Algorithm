import math
N = input()
while True:
    for i in N:
        if i not in '47':
            N = str(int(N)-1)
            break
    else:
        print(N)
        exit()

