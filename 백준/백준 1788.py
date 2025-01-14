input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline 
n=int(input())
dp=[0 for _ in range(abs(n)+1)]
dp[0]=0
if abs(n)>0:
    dp[1]=1
for i in range(abs(n)-1):
    dp[i+2]=(dp[i+1]+dp[i]) %1000000000
if n>0:
    print(1)
    print(dp[n])
elif n==0:
    print(0)
    print(dp[n])
elif n<0:
    if abs(n) % 2==0:
        print(-1)
    else:
        print(1)
    print(dp[abs(n)])