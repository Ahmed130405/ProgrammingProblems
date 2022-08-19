import itertools
if __name__ == '__main__':
    def sieve(gen,n):
        return itertools.filterfalse(lambda x: x%n==0, gen)
    gen = itertools.count(2)
    for i in range(2,10002):
        j = next(gen)
        gen = sieve(gen,j)
    print(next(gen))