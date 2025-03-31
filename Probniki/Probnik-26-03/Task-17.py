with open('1706.txt') as file:
    data = [int(i) for i in file]

min_19 = min([i for i in data if str(i)[-2:] == '19' and len(str(abs(i))) == 3])

ans = []

for i in range(len(data) - 2):
    a1, a2, a3, = data[i], data[i + 1], data[i + 2]


    u1 = str(a1)[-2:] == '19' and len(str(abs(a1))) == 5
    u2 = str(a2)[-2:] == '19' and len(str(abs(a2))) == 5
    u3 = str(a3)[-2:] == '19' and len(str(abs(a3))) == 5

    f1 = u1 + u2 + u3 >= 1
    f2 = a1 + a2 + a3 > min_19 ** 2

    if f1 and f2:
        ans.append(a1 + a2 + a3)

print(len(ans), min(ans))



