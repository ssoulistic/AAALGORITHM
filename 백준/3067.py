input=open("sample.txt","r").readline
# import sys
# input=sys.stdin.readline
T=int(input())
for _ in range(T):
    N=int(input())
    coins=list(map(int,input().split()))
    M=int(input())
    dp=[0 for _ in range(M+1)]
    dp[0]=1
    for i in range(1,N+1):
        for j in range(M+1):
            if j>=coins[i-1]:
                dp[j]+=dp[j-coins[i-1]]
    print(dp[-1])