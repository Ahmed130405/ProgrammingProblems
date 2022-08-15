# even terms are in steps of 3

import itertools

def fib():
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a+b

seq=fib()
index=0
while not (next(seq)>4000000):
    index+=1

print(sum(list(itertools.islice(fib(),1,index,3))))
