from itertools import product


cnt = 0
for val in product('КОТБУС', repeat=8):
    val = ''.join(val)
    if val[0] != 'О' and val[0] != 'У' and val.count('КОТ') >= 1:
        cnt += 1

print(cnt)
