from itertools import product

for r in range(4):
    for i in product('0123456789', repeat = r):
        i = ''.join(i)
        i = int('1234' + i + '7')
        if i <= 10**8 and i % 141 == 0:
            print(i, i // 141)
