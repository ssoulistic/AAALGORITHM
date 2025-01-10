input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N,M,K=map(int,input().split())
dp=[[0  for _ in range(K+1)] for _ in range(M+1)]
for _ in range(N):
    x,y=map(int,input().split())
    for j in range(M,x-1,-1):
        for k in range(K,y-1,-1):
            dp[j][k]=max(dp[j-x][k-y]+1,dp[j][k])
print(*dp,sep="\n")
print(dp[-1][-1])