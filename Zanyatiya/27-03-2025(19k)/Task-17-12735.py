with open('17_12735.txt') as file:
    data = [int(i) for i in file]

max_09 = max([i for i in data if str(i)[-2:] == '09'])

ans = []

for i in range(len(data) - 2):
    a1, a2, a3 = data[i], data[i+1], data[i+2]

    u1 = a1 % 7 == 0
    u2 = a2 % 7 == 0
    u3 = a3 % 7 == 0

    f1 = u1 + u2 + u3 == 2

    if f1 and a1 + a2 + a3 < max_09:
        ans.append(a1 * a2 * a3)

print(len(ans), min(ans))