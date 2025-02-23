from itertools import product

ans = []
for r in range(4):
    for z in product('123456789', repeat=r):
        z = ''.join(z)
        for x in product('0123456789', repeat=r):
            x = ''.join(x)
            num = int(z + '15' + x + '7424')
            if num % 127 == 0  and num <= 10**8:
                ans.append([num, num//127])

ans = sorted(ans)
for i in ans:
    print(*i)
