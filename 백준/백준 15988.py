input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline 
T=int(input())
dp=[0 for _ in range(1000001)]
dp[1]=1
dp[2]=2
dp[3]=4
for i in range(1,1000001-3):
    dp[i+3]=(dp[i+2]+dp[i+1]+dp[i]) % 1000000009
for _ in range(T):
    print(dp[int(input())])