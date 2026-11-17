a=[]
f = open("22.txt")
for s in f :
    a.append(list(map(int, s.split())))
a.sort()
t={0:0}
for i in range(len(a)):
    y=[t[x]+a[i][1] for x in a[i][2:]]
    t[a[i][0]]=max(y)
print(max(t.values()))
print(t)
