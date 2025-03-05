from itertools import product

ans = []
for v in '0123456789':
    for r in '0123456789':
        for x in '0123456789':
            num = int('12' + v + '345' + r + '67089' + x)
            if num <= 10**13 and num % 206 == 0:
                ans.append([num, num // 206])

ans = sorted(ans)
for i in ans:
    print(*i)
