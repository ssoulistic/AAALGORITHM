input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
T=int(input())
for _ in range(T):
    N=int(input())
    coins=list(map(int,input().split()))
    M=int(input())
    dp=[[0 for _ in range(N)] for _ in range(M)]
    # 열 = 1~M까지의 금액 을 만들 수 있는 경우의 수
    for i in range(N):
        if M>coins[i]-1>=0:
            dp[coins[i]-1][i]=1
        for money in range(M):
            if money-coins[i]>=0:
                dp[money][i]+=sum(dp[money-coins[i]])
    print(sum(dp[M-1]))

