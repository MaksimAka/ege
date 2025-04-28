from itertools import product

cnt = 0
for i in product('0123456789ABCDE', repeat = 7):
    i = ''.join(i)
    if i[0] != '0' and i.count('0') == 2:
        for j in 'ABCDE':
            i = i.replace(j, 'm')
        if i.count('m') <= 3:
            cnt += 1

print(cnt)
