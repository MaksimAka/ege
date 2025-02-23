from itertools import product

ans = []
for r in range(3):
    for z in product('0123456789', repeat=r):
        z = ''.join(z)
        for v in '0123456789':
            for x in '0123456789':
                for c in '0123456789':
                    num = int('12' + v + '3' + z + '456' + x + c + '9')
                    if num % 98591 == 0 and num <= 10**12:
                        ans.append([num, num//98591])

ans = sorted(ans)
for i in ans:
    print(*i)
