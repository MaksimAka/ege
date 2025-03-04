from itertools import product

ans = []
for r in range(7):
    for z in product('0123456789', repeat=r):
        z = ''.join(z)
        for v in '02468':
            num = int(v + '136' + z)
            if num % 53191 == 0 and num <= 10**10:
                ans.append([num, num//53191])

ans = sorted(ans)
for i in ans:
    print(*i)

#perereshat'