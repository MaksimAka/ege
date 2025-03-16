def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]



ans = []
for N in range(1, 10000):
    R = convert(N, 3)
    if N % 3 == 0:
        R = R + R[-2:]
    else:
        R = R + convert(5*(N % 3), 3)

    R = int(R, 3)
    if R > 133:
        ans.append(R)

print(min(ans))
