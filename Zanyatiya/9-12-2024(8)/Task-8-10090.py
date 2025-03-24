from itertools import product

cnt = 0
for i in product('01234567', repeat = 5):
    i = ''.join(i)
    if '1' not in i and len(i) == len(set(i)) and i[0] != '0':
        for j in range(4):
            if int(i[j]) % 2 == int(i[j+1]) % 2:
                break
        else:
                cnt += 1
print(cnt)