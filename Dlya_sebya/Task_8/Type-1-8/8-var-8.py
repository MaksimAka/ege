from itertools import product

cnt = 0
alf = sorted('ИНТЕГРАЛ')
for pos, val in enumerate(product(alf, repeat = 5), start = 1):
    val = ''.join(val)
    if pos % 2 != 0 and val[0] != 'Т' and 1 <= val.count('Н') <= 2:
        cnt += 1


print(cnt)