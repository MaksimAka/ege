def f(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (x < A) and (y < A) and (x * y > 1200)
            if f:
                return False
    return True

for A in range(0, 1000)[::-1]:
    if f(A):
        print(A)
        break