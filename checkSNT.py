import math

def prime(n):
    if(n < 2):
        return False
    for i in range(2,math.isqrt(n)+1,1):
        if (n % i == 0):
            return False
    return True

t = int(input())
if prime(t):
    print("YES")
else:
    print("NO")
