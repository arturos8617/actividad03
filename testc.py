from math import factorial


def numberfac(n):
    return(factorial(n))


total = 0
limit = int(input())
n = 0
while(n <= limit):
    total += (1/numberfac(n))
    n = n+1

print(total)
