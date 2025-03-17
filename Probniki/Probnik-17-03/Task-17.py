with open('17_14952.txt') as file:
    data = [int(i) for i in file]

max_121 = max([i for i in data if str(i)[-3:]=='121'])
ans = []

for i in range(len(data)-2):
    a1, a2, a3 = data[i], data[i+1], data[i+2]

    u1 = (1000 <= abs(a1) <= 9999) and a1 % 2 == 0
    u2 = (1000 <= abs(a2) <= 9999) and a2 % 2 == 0
    u3 = (1000 <= abs(a3) <= 9999) and a3 % 2 == 0
    f1 = u1 + u2 + u3 <= 1

    if f1 and (a1 + a2 + a3) <= max_121:
        ans.append(a1 + a2 + a3)

print(len(ans), max(ans))