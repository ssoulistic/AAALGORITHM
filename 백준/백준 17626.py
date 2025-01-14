input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
T=int(input())
def four_square(n,count,mini):
    part1=int(n**(1/2))
    if n==part1**2:
        return count
    
    for first in range(part1,part1//(5-count),-1):
        x=four_square(n-first**2,count+1,mini)
        if x and x<=4:
            if mini>x:
                mini=x
    return mini

print(four_square(T,1,5))