def automatic(n):
    n2=bin(n)[2:]
    #n2+=str(n2.count('1') % 2)
    #n2+=str(n2.count('1') % 2)
    if n%2==0:
        n2+='01'
    else:
        n2+='10'
    return(int(n2, 2))
minn=10**5
for n in range(10**5):
    if automatic(n) > 102 and automatic(n) < minn:
        minn = automatic(n)
print(minn)
def auto(n):
    n0=int(str(n)[0])+int(str(n)[1])
    n1=int(str(n)[1])+int(str(n)[2])
    return(str(max([n0,n1])) + str(min([n0,n1])))
s=0
for n in range(10**2,10**3):
    if auto(n) == "1715":
        s+=1
print(s)
