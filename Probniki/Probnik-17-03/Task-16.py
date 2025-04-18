from functools import lru_cache

@lru_cache(None)
def F(n):
    if n > 7000:
        return n + 4
    if n <= 7000:
        return 3*n + 5 + F(n + 3)

for i in range(7000, 0, -1):
    F(i)

print(F(707) - F(716))