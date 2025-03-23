from itertools import product

cnt = 0
for i in product('012345678', repeat = 5):
    i = ''.join(i)
    if i.count('0') == 1 and i[0] != '0' and '01' not in i and '03' not in i and '05' not in i \
    and '07' not in i and '10' not in i and '30' not in i and '50' not in i and '70' not in i:
        cnt += 1
print(cnt)