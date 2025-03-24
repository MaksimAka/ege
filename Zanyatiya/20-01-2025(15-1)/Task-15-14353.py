def tre(n, m, k):
    if n < m + k and m < n + k and k < n + m:
        return max(A)

def maks(a, b):
    if a > b:
        return a
    else:
        return b


def f(A):
    for x in range(1, 1000):
        f = (tre(A, 7, x)) <= (27 == (not(tre(36, 21, x))))

for A in range(1, 1000)[::-1]:
    if f(A):
        print(A)
        break

