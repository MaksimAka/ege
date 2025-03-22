from itertools import product

ans = []
alf = sorted('ФОКУС')
for pos, val in enumerate(product(alf , repeat=5), start=1):
    val = ''.join(val)
    if val.count('Ф') == 0 and val.count('У') == 2:
        ans.append(pos)
print(max(ans))
