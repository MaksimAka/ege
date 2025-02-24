from itertools import product

ans = []
for r in range(3):
    for z in product('123456789', repeat=r):
        z = ''.join(z)
        for r2 in range(3-r):
            for x in product('0123456789', repeat=r2):
                x = ''.join(x)
                num = int(z + '15' + x + '7424')
                if not (num % 127 == 0 and num % 111 == 0) \
                        or (num % 127 == 0 and num % 113 == 0) \
                        or (num % 111 == 0 and num % 113 == 0):
                    if num % 127 == 0 and num <= 10**8:
                        ans.append([num, num//127])
                    if num % 111 == 0 and num <= 10**8:
                        ans.append([num, num//111])
                    if num % 113 == 0 and num <= 10 ** 8:
                        ans.append([num, num // 113])
ans = sorted(ans)
for i in ans:
    print(*i)
