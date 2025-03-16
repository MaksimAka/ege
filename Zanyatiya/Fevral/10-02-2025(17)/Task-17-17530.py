with open('17_17530.txt') as file:
    data = [int(i) for i in file]

minn = min(data)

ans = []
for i in range(len(data)-1):
    a1, a2 = data[i], data[i+1]

    u1 = a1 % 55 == minn
    u2 = a2 % 55 == minn

    if u1 + u2 >= 1:
        ans.append(a1 + a2)

print(len(ans), min(ans))

