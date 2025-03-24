from itertools import product

cnt = 0
for i in product('012345', repeat = 6):
    i = ''.join(i)
    if i.count('0') == 1 and '01' not in i and '03' not in i and '05' not in i and '10' not in i\
    and '30' not in i and '50' not in i and i[0] != '0':
        cnt += 1

print(cnt)



from itertools import product

cnt = 0
for i in product('012345', repeat = 6):
    i = ''.join(i)
    if i.count('0') == 1 and i[0] != '0':
        for k in '135':
            i = i.replace(k, 'g')
        if 'g0' not in i and '0g' not in i:
            cnt += 1

print(cnt)