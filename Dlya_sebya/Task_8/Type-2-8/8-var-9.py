from itertools import product

cnt = 0
for i in product('01234567', repeat = 5):
    i = ''.join(i)
    if i.count('4') == 2 and '41' not in i and '43' not in i and '45' not in i and '47' not in i and '14' not in i\
    and '34' not in i and '54' not in i and '74' not in i and i[0] != '0':
        cnt += 1

print(cnt)