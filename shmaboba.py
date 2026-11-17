import functools
@functools.lru_cache()
def g(x):
    if x < 10:
        return(x)
    return(g(f(x)))
def f(x):
    if x == 1:
        return(5)
    return(f(x-1)/(1+f(x-1)))

print(f(12))
