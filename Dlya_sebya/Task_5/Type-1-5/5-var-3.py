ans = []

for N in range(1, 1000):
    R = bin(N)[2:]
    if N % 4 == 0:
        R = R + R
    else:
        R = R + R[::-1]
    R = int(R, 2)
    if R >= 544:
        ans.append(N)

print(min(ans))