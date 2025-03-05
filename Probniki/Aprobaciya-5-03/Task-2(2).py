from itertools import permutations, product

def f(x, y, z, w):
    return (not (z <= y)) or (x <= w) or (not x)
for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat = 7):
    table = [(0, 1, a1, a2), (a3, 0, a4, a5), (1, a6, 0, a7)]
    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]
            if u:
                print(*p)