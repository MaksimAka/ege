ans = []

for N in range(1, 10000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = R + '0'
    else:
        R = R + '1'
    if R.count('1') % 3 == 0:
        R = '11' + R[2:]
    else:
        R = '10' + R[2:]

    R = int(R, 2)
    if R <= 37:
        ans.append(N)
print(max(ans))