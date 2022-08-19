if __name__ == '__main__':
    # brute force search lol
    num=0
    for i in range(1000,100,-1):
        for j in range(1000,100,-1):
            if str(i*j) == str(i*j)[::-1]:
                if i*j>num:
                    num=i*j
                print(num)
                break
        
