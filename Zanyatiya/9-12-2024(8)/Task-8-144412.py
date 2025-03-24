from itertools import product

cnt = 0
for i in product('алгоритм', repeat = 6):
    i = ''.join(i)
    if i.count('л') <= 1 and i[0] != 'р' and i[-1] not in 'лгртм':
        cnt += 1


print(cnt)