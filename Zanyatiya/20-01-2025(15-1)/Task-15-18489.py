def cif(x, y):
    return str(x)[-1:] == str(y)[-1:]

def f(A):
    for x in range(1, 1000):
        f = (not(cif(x, 5)) and cif(x, 4)) <= (x > A - 11)
        if not f:
            return False
    return True

for A in range(1, 1000)[::-1]:
    if f(A):
        print(A)
        break