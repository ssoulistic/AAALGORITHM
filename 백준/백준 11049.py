input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
matrix=[]
dp = [[1e9 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    a,b = map(int,input().split())
    matrix.append((a,b))

for diff in range(N):
    for r in range(N-diff):
        c=r+diff
        if r==c:
            dp[r][c]=0
        for i in range(diff):
            dp[r][c]=min(dp[r][c],dp[r+i+1][c]+dp[r][c-diff+i]+matrix[r][0]*matrix[c-diff+i][1]*matrix[c][1])
print(dp[0][N-1])

