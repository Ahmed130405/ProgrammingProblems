import math as m
import itertools
import functools

def factorGen(n):
    d=2
    mult=0
    while n>1:
        while n%d==0:
            n=n/d
            mult+=1
        if mult>0:
            yield (d,mult)
        d+=1
        mult=0

def divisorGen(n):
    factors = list(factorGen(n))
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield functools.reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return

def isStealthy(n):
    isStealthy=0
    for i in divisorGen(n):
        for j in divisorGen(n):
            if (i+n//i)==(j+n//j+1):
                isStealthy=1
                break
        if isStealthy==1:
            break
    return isStealthy

count=0
for i in range(2,10**4+1):
    count+=isStealthy(i)

print(count)
