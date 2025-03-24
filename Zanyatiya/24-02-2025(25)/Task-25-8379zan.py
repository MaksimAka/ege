from fnmatch import fnmatch
for i in range(123405708 - 123405708 % 137, 10**10, 137):
    if fnmatch(str(i),'1234*'):
        print(i, i // 137)

#perereshat'