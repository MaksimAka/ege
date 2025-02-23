from itertools import product

ans = []
for r in range(6):
    for z in product('02468', repeat=r):
        z = ''.join(z)
        for v in '13579':
            for x in '13579':
                num = int(z + '12' + v + '4' + x)
                if num % 9231 == 0 and num <= 10**10:
                    ans.append([num, num//9231])

ans = sorted(ans)
for i in ans:
    print(*i)
