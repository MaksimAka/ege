from fnmatch import fnmatch

for i in range(123405 - 123405 % 21025, 10**10, 21025):
    if fnmatch(str(i),'12*34?5'):
            print(i, i//21025)