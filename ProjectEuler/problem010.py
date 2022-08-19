import itertools
import math as m
if __name__ == '__main__':
    def isPrime(n):
        if n<=3:
            return True
        if(n%2==0 or n%3==0):
            return False
        for i in range(5,int(m.sqrt(n)+1),6):
            if(n%i==0 or n%(i+2)==0):
                return False
        return True
    def nextPrime(n):
        n+=1
        while not isPrime(n):
            n+=1
        return n
    p=2
    sum=0
    while p<2000000:
        sum+=p
        p=nextPrime(p)
    print(sum)
