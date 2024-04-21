input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
from collections import deque
N=int(input())
house=[]
for _ in range(N):
    house.append(list(map(int,input().split())))
count=0
dp=[[[0,0,0] for _ in range(N)] for _ in range(N)]
dp[0][1]=[1,0,0]
for r in range(N):
    for c in range(N):
        # 가로 이동
        if 0<=r<N and 0<=c+1<N:
            if house[r][c+1]!=1:
                dp[r][c+1][0] += dp[r][c][0]+dp[r][c][2]
        # 세로
        if 0<=r+1<N and 0<=c<N:
            if house[r+1][c]!=1:
                dp[r+1][c][1] += dp[r][c][1]+dp[r][c][2]
        # 대각선
        if 0<=r+1<N and 0<=c+1<N:
            if house[r+1][c]!=1 and house[r][c+1]!=1 and house[r+1][c+1]!=1:
                dp[r+1][c+1][2]+=sum(dp[r][c])

for d in dp:
    print(d)
print(sum(dp[N-1][N-1]))