from fnmatch import fnmatch

for i in range(851604 - 851604 % 2658, 10**9, 2658):
    if fnmatch(str(i),'85*16?4'):
            print(i, i//2658)