
def solut(l, p, v):
    n = v // p
    m = min(l, v%p)

    return n*l + m

t = 1
while True:
    l ,p, v = map(int, input().split())
    if l == p == v == 0:
        break
    print('Case {}: {}'.format(t, solut(l, p, v)))
    t +=1

