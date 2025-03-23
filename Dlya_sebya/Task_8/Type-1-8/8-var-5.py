from itertools import product

ans = []
cnt = 0
alf = sorted('фаворит')
for pos, val in enumerate(product(alf, repeat = 6), start = 1):
    val = ''.join(val)
    if pos % 2 == 0 and val[0] != 'о' and val.count('р') == 2:
        cnt += 1
        ans.append(pos)

print(cnt, len(ans))