input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
N,K=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(N-1):
    A,B=map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)
V=list(map(int,input().split()))
target=[False for _ in range(N+1)]
for v in V:
    target[v]=True
visited=[False for _ in range(N+1)]
dp=[0 for _ in range(N+1)]
def dfs(cur):
    visited[cur]=True
    for nc in graph[cur]:
        if not visited[nc]:
            dp[cur]+=dfs(nc)
    if target[cur]:
        dp[cur]+=1
    return dp[cur]
dfs(V[0])
print(N-dp.count(0)+1)
