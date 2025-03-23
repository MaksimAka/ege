from itertools import product

ans = []
alf = sorted('сорняк')
for pos, val in enumerate(product(alf, repeat = 6), 1):
    val = ''.join(val)
    if val.count('к') <= 3 and val.count('я') == 2:
        ans.append(pos)

print(min(ans), ans[0])