input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
work=[]
# 1<<N -1 
dp=[10**6 for _ in range(1<<N)]
dp[0]=0
for _ in range(N):
    work.append(list(map(int,input().split())))
for i in range(1<<N):
    k=0
    for j in range(N):
        if i & (1<<j):
            k+=1
    for j in range(N):
        if i & (1<<j) == 0 and dp[i|(1<<j)]>dp[i]+work[k][j]:
            dp[i|(1<<j)]=dp[i]+work[k][j]
        print(i,j,k,dp)
print(dp[-1])