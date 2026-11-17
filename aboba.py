зад.9
'''def check(s):
    s=list(map(int, s.split()))
    mid = sum(s) / 8
    y = [q for q in s if q %2 == 1]
    z = [q for q in s if q %2 ==0]
    n = [q for q in s if (q % 2 ==0 and q > mid)]
    m = [q for q in s if (q % 2 == 1 and q > mid)]
    if len(n) > len(m) and sum(z) < sum(y):
        return 1
    else: 
        return 0
x = [s for s in open("abobaboba.txt") if check(s)]
print(len(x))'''
зад.22
'''a=[]
f = open("22.txt")
for s in f :
    a.append(list(map(int, s.split())))
a.sort()
t={0:0}
for i in range(len(a)):
    y=[t[x]+a[i][1] for x in a[i][2:]]
    t[a[i][0]]=max(y)
print(max(t.values()))
print(t)'''
зад.5
'''def automatic(n):
    n2=bin(n)[2:]
    n2+=str(n2.count('1') % 2)
    n2+=str(n2.count('1') % 2)
    return(int(n2, 2))
minn=10**5
for n in range(10**5):
    if automatic(n) > 125 and n < minn:
        minn = n
print(minn)
def auto(n):
    n0=int(str(n)[0])+int(str(n)[1])
    n1=int(str(n)[1])+int(str(n)[2])
    return(str(max([n0,n1])) + str(min([n0,n1])))
s=0
for n in range(10**2,10**3):
    if auto(n) == "1715":
        s+=1
print(s)'''
зад.16
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
