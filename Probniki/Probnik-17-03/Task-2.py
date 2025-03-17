print('w x y z')
for x in 1, 0:
    for y in 1, 0:
        for z in 1, 0:
            for w in 1, 0:
                f = not(x == (w and (not z))) and (y == (x and (not w)))
                if f:
                    print(w, x, y, z)