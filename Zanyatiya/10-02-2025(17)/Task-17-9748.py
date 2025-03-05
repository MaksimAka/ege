with open('17_9748.txt') as file:
    data = [int(i) for i in file]

max_15 = max([i for i in data if str(i)[-2:] == '15'])

ans = []

for i in range(len(data) - 2):
    a1, a2, a3, = data[i], data[i + 1], data[i + 2]


    u1 = len(str(a1)) == 4            #количество символов = 4
    u2 = 1000 <= a2 <= 9999           #все четырёхзначные числа находятся в этом промежутке
    u3 = 1000 <= a3 <= 9999           #проверка на четырёхзначность (2 способа)

    f1 = u1 + u2 + u3 == 1
    f2 = a1 + a2 + a3 >= max_15

    if f1 and f2:
        ans.append(a1 + a2 + a3)

print(len(ans), max(ans))

