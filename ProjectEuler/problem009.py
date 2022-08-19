if __name__ == '__main__':
    sum=False
    for s in range(500):
        for t in range(s):
            a=2*s*t
            b=s**2-t**2
            c=s**2+t**2
            if a+b+c==1000:
                sum=True
                break
        if sum:
            break
    print(a*b*c)
