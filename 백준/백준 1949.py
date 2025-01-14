input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline 
N=int(input())
neighbors=list(map(int,input().split()))
graph=[[] for _ in range(N)]
for _ in range(N-1):
    s,e=map(int,input().split())
    graph[s-1].append(e-1)
    graph[e-1].append(s-1)
dp=[[0,0] for _ in range(N)]
visited=[False for _ in range(N)]
def dfs(cur_node):
    visited[cur_node]=True
    for next_node in graph[cur_node]:
        if not visited[next_node]:
            results=dfs(next_node)
            dp[cur_node][0]+=results[1]
            dp[cur_node][1]+=max(results)
    dp[cur_node][0]+=neighbors[cur_node]
    return dp[cur_node]

dfs(0)
print(max(dp[0]))