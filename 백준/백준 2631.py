input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
# LIS 문제
line=[]
for _ in range(N):
    line.append(int(input()))
dp=[0 for _ in range(N)] # idx, 가장 큰 수
for i in range(N):
    dp[i]=1
    for j in range(i):
        if line[i]>line[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(N-max(dp))
