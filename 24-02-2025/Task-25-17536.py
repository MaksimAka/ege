def f(num):
    dell = []
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            dell.append(i)
            dell.append(num // i)
    dell = (set(dell))

    if len(dell) <= 1:
        return 0
    return min(dell) + max(dell)

cnt = 0
for i in range(800_001, 10**30):
    M = f(i)
    if M % 10 == 4:
        print(i, M)
        cnt += 1
        if cnt == 5:
            break


