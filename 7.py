'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?'''



import math
def issimple(n):
    r=math.ceil(math.sqrt(n))
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=5
s=[2,3]
while True:
    if issimple(n) is True:
        s.append(n)
    if len(s)==10001:
        break
    n+=2

print(s[-1])