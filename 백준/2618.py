input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
W=int(input())
dp=[[[[1e9 for _ in range(N+1)] for _ in range(N+1)] for _ in range(W+1)] for _ in range(2)]
C1=[1,1]
C2=[N,N]
dp[0][0][1][1]=0
dp[0][0][N][N]=0
for i in range(1,W+1):
    r,c=map(int,input().split())
    dp[0][i][r][c]=min(dp[0][i][r][c],dp[0][i-1])
    

