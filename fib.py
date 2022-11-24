from functools import lru_cache

@lru_cache()
def recursiveFibCached(n):
    if n == 1 or n == 2:
        return 1

    return recursiveFibCached(n - 1) + recursiveFibCached (n - 2)

print(recursiveFibCached(500))