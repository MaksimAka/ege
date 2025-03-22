from itertools import product

cnt = 0
for i in product('0123', repeat = 3):
    i = ''.join(i)
    if int(i[0]) >= int(i[1]) >= int(i[2]) and i[0] != '0':
        cnt +=1

print(cnt)
