import math as m
if __name__ == '__main__':
    n=600851475143
    for i in range(int(m.sqrt(n)),0,-1):
        if n % i==0:
            print(i) # choose second-to-last value
            n = i
            if n == 1:
                break
