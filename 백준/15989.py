input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
T=int(input())
dp=[[0,0,0]]*10001
dp[1]=[1,0,0]
dp[2]=[1,1,0]
dp[3]=[2,0,1]
for i in range(2,9999):
    dp[i+2]=[sum(dp[i+1]), dp[i][1]+dp[i][2], 0 if (i+2) % 3 else 1 ]
for _ in range(T):
    print(sum(dp[int(input())]))