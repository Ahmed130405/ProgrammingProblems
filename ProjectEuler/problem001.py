sum = 0
for i in range(10):
    if i % 3 | i % 5:
        sum += i
print(sum)
