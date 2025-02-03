input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N = int(input())
P=list(map(int,input().split()))
dp=[float("inf") for _ in range(N+1)]
dp[0]=0

for i in range(1,N+1):
    for j in range(i,N+1):
        dp[j]=min(dp[j-i]+P[i-1],dp[j])
print(dp[-1])