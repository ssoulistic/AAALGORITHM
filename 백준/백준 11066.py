input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline 
T=int(input())
for _ in range(T):
    K=int(input())
    file_sizes=list(map(int,input().split()))
    acc_fs=[0]*(K+1)
    for p in range(K):
        acc_fs[p+1]=acc_fs[p]+file_sizes[p]
    dp=[[0]*K for _ in range(K)]
    for length in range(1,K+1):
        for row in range(K-length):
            col=row+length
            dp[row][col]=float("inf")
            for i in range(length):
                if dp[row][col]>dp[row+length-i][col]+dp[row][col-1-i]+acc_fs[col+1]-acc_fs[row]:
                    dp[row][col]=dp[row+length-i][col]+dp[row][col-1-i]+acc_fs[col+1]-acc_fs[row]
    print(dp[0][K-1])

        