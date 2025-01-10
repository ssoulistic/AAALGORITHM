input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
D,P=map(int,input().split())
dp=[0 for _ in range(D+1)]
dp[0]=2**24
for k in range(P):
    L,C=map(int,input().split())
    for i in range(D,L-1,-1):
        if dp[i-L]:
            dp[i]=max(dp[i],min(dp[i-L],C))
print(dp[-1])
    