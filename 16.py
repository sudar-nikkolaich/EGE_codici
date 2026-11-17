'''f = [0]* 101
f[0]=1
f[1]=1
q= [0]*6
q[0]=0
q[1]=1
for i in range (2, 101):
    if i <= 3:
        f[i]=i
    elif i % 3 == 0:
        f[i]= i**3 + f[i-1]
    elif i% 3 == 1:
        f[i]= 4+ f[i//3]
    elif i%3 ==2:
        f[i]=i**2 + f[i-2]
print(f[100])'''
import functools
@functools.lru_cache()
def g(x):
    if x < 10:
        return(x)
    return(g(f(x)))
def f(x):
    if x == 1:
        return(1)
    return(f(x-1) + 2 ** (x - 1))

print(f(12))
