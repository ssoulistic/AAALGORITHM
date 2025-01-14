input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
# N 자리 이친수 => 11연속 x 0시작 x
# 1 자리 => 1
# 2자리 => 10
# 3자리 => 101 100
dp=[[0,0] for _ in range(N)]
dp[0][1]=1
for i in range(N-1):
    dp[i+1][0]=dp[i][0]+dp[i][1]
    dp[i+1][1]=dp[i][0]
print(sum(dp[N-1]))