def squaresum(n):
    sm = 0
    for i in range(1, n+1):
        sm = sm + (i * i)
    return sm

n = int(input('enter a number:'))
print(squaresum(n))