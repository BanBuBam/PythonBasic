import math
def thuannghich(n):
    if n < 10:
        return False
    else:
        rev = 0
        temp = n
        while n != 0:
            rev = rev * 10 + n %10
            n //= 10
        if(rev == temp ):
            return True
        else:
            return False
if __name__ == '__main__':

    t = int(input())
    while t > 0:
        x = input()
        tong =0
        for i in x:
            tong += int(i)
        if thuannghich(tong):
            print("YES")
        else:
            print("NO")
        t-=1