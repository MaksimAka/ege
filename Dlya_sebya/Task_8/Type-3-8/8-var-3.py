from itertools import product

cnt = 0
for i in product('123456', repeat = 4):
    i = ''.join(i)
    if i.count('3') == 1:
        cet = sum(1 for c in i if c in '246')
        necet = sum(1 for c in i if c in '135')
        if cet <= necet:
            cnt += 1
print(cnt)
