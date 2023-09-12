import math
t = int(input())
while(t > 0):
    s = input()
    res = 0
    check = 0
    if len(s) <= 3:
        print("NO")
    else:
        for i in range(1,len(s),1):
            if s[i-1]  < s[i]:
                res+=1
            else:
                break
        
        for i in range(res+1,len(s),1):
            if s[i-1] < s[i]:
                check =1
        if check ==1:
            print("NO")
        else:
            print("YES")
    t-=1