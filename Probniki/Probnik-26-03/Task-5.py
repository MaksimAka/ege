def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 1000):
    R = convert(N, 4)
    if sum(map(int, R)) % 2 == 0:
        R = R + R[-2:]
    else:
        R = '2' + R + '0'

    R = int(R, 4)
    if R % 2 == 0 and R > 120:
        ans.append(R)

print(min(ans))
