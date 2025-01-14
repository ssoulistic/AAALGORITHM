input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline 
N=int(input())
pr=[0]+list(map(int,input().split()))
dp=[0 for _ in range(N+1)]
for k in range(1,N+1):
    for i in range(N+1):
            if k-i>=0:
                dp[k]=max(dp[k],dp[k-i]+pr[i])
print(dp[N])