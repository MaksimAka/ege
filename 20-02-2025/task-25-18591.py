from itertools import product

ans = []

for v in '0123456789':
    for H in '13579':
        for X in '02468':
            for C in '02468':
                for d in '0123456789':
                    num = int(X + '9' + v +'23' + d + '23' + H + C)
                    if num <= 10**10 and num % 1984 == 0:
                        ans.append([num, num//1984])


ans = sorted(ans)
for i in ans:
    print(*i)