import math

def prime(n):
    if(n < 2):
        return False
    for i in range(2,math.isqrt(n)+1,1):
        if (n % i == 0):
            return False
    return True

t = int(input())
while(t >0):
    n = input()
    dem1=0
    dem2=0
    for i in n:
        if prime(int(i)):
            dem1+=1
        else:
            dem2+=1
    if prime(dem1+dem2) and dem1 > dem2:
        print("YES")
    else: 
        print("NO")
    t-=1
