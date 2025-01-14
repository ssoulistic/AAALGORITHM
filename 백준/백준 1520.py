input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline

M,N=map(int,input().split())
graph=[]
dp=[[0 for _ in range(N)] for _ in range(M)]
dp[M-1][N-1]=1
for _ in range(M):
    graph.append(list(map(int,input().split())))

search=[[1,0],[0,1],[-1,0],[0,-1]]
def dfs(r,c):
    if dp[r][c]:
        return dp[r][c]
    
    for dr,dc in search:
        nr=r+dr
        nc=c+dc
        if 0<=nr<M and 0<=nc<N and graph[nr][nc]<graph[r][c] and graph[nr][nc]>=graph[M-1][N-1]:
            dp[r][c]+=dfs(nr,nc)
    if dp[r][c]==0:
        graph[r][c]=1e9
    return dp[r][c]
dfs(0,0)
print(*dp,sep='\n')
print(*graph,sep='\n')
print(dp[0][0])