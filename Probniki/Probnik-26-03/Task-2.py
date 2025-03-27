print('w y x z')
for x in 0, 1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                f = x and ((z <= y) == w)
                if f:
                    print(w, y, x, z)