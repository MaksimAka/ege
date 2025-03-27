def f(start, end):
    if start == end:
        return 1
    if start > end or start == 8:
        return 0
    return f(start + 1, end) + f(start * 2, end) + f(start * 5, end)

print(f(2, 27) * f(27, 54))