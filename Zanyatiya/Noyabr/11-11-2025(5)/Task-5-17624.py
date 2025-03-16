ans = []

for N in range(1, 1000):
    R = bin(N)[2:]
    if sum(map(int, R)) % 2 == 0:
        R = R + '0'
    else:
        R = R + '1'
    if sum(map(int, R)) % 2 == 0:
        R = R + '0'
    else:
        R = R + '1'
    R = int(R, 2)
    if R > 75:
        ans.append(R)

print(min(ans))
