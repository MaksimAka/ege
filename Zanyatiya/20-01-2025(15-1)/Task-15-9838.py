def f(A):
    for x in range(0, 1000):
        for y in range(0, 1000):
            f = (x + 2 * y > A) or (y < x) or (x < 30)
            if not f:
                return False
    return True

for A in range(0, 1000)[::-1]:
    if f(A):
        print(A)
        break