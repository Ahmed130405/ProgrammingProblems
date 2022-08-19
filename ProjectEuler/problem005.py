import math as m
if __name__ == '__main__':
    num = 2520
    for i in range(11,21):
        num=m.lcm(num,i) # Python 3.9+
    print(num)

    