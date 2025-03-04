#1 способ
from functools import lru_cache
from sys import setrecursionlimit

#@lru_cache(None) конфликтует с from sys import setrecursionlimit
def F(n):
    if n < 11:
        return n
    if n >= 11:
        return n + F(n - 1)

setrecursionlimit(3000)
print(F(2024) - F(2021))


#2 способ (лучше)
from functools import lru_cache

@lru_cache(None)
def F(n):
    if n < 11:
        return n
    if n >= 11:
        return n + F(n - 1)

for i in range(2025):
    F(i)
#Позволяет не пользоваться from sys import setrecursionlimit
print(F(2024) - F(2021))