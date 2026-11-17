def check(s):
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
print(len(x))
