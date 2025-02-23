from itertools import product

ans = []
for r in range(5):
    for z in product('0123456', repeat=r):
        z = ''.join(z)
        num = int('213' + z + '5664')
        if num % 333 == 0 and num <= 10**9:
            ans.append([num, num//333])

ans = sorted(ans)
for i in ans:
    print(*i)
