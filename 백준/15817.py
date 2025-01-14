input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N,x=map(int,input().split())
dp=[0 for _ in range(x+1)]
dp[0]=1
for _ in range(N):
    L,C=map(int,input().split())
    for j in range(1,C+1):
        for i in range(x,L*j-1,-1):
            dp[i]+=dp[i-L*j]
print(dp)
print(list(i for i in range(len(dp))))