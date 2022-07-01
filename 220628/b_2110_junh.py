
def solut():
    pass

N, C = map(int, input().split())
dist = 0
houses = sorted(int(input()) for _ in range(N))
chosen = {0, N-1}
print(chosen)
