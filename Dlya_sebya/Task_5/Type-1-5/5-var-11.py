ans = []

for N in range(1, 10000):
    R = bin(N)[2:]
    if len(R) % 2 == 0:
        R =  R[:len(R)//2] + '1' + R[len(R)//2:]
    else:
        R
    R = int(R, 2)
    if R >= 26:
        ans.append(N)

print(min(ans))