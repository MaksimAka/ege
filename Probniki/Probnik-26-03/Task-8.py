from itertools import product

alf = sorted('ЛУНАТИК')
for pos, val in enumerate(product(alf, repeat = 6), 1):
    val = ''.join(val)
    if val.count('У') == 1 and val[0] == 'Н':
        print(pos)

print(int('465555', 7))