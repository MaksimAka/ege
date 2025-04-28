R = '1111'
if len(R) % 2 == 0:
    R = R[:len(R) // 2 - 1] + R[len(R) // 2 + 1:]
else:
    R = R[:len(R) // 2 - 1] + R[len(R) // 2 + 2:]
print(R)
