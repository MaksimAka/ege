from itertools import product

ans = []
for r in range(5):
    for z in product('0123456789', repeat=r):
        z = ''.join(z)
        for v in '0123456789':
            num = int('12' + z + '567' + v)
            if num % 7777 == 0 and num <= 10**10 and num % 2 == 0:
                ans.append([num, num//7777])

ans = sorted(ans)
for i in ans:
    print(*i)