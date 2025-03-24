def f(num):
    dell = []
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            dell.append(i)
            dell.append(num//i)
    dell = sorted(set(dell))

    for i in dell:
        if i % 10 == 8 and i != 8:
            return i
    return 0

cnt = 0
for i in range(500001, 10**20):
    res = f(i)
    if res:
        print(i, res)
        cnt += 1
        if cnt == 5:
            break




