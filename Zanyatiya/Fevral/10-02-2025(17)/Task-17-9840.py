with open('17_9840.txt') as file:
    data = [int(i) for i in file]

max_39 = max([i for i in data if str(i)[-2:] == '39' and len(str(abs(i))) == 4])

ans = []

for i in range(len(data)-1):
    a1, a2 = data[i], data[i+1]

    u1 = len(str(abs(a1))) == 4
    u2 = len(str(abs(a2))) == 4

    f1 = u1 + u2 == 1
    f2 = (a1 + a2)**2 <= max_39 ** 2

    if f1 and f2:
        ans.append(a1+a2)

print(len(ans), abs(max(ans)))