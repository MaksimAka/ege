def f(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (x + y <= 22) or (y <= x - 6) or (y >= A)
            if not f:
                return False
    return True

for A in range(0, 1000)[::-1]:
    if f(A):
        print(A)
        break
