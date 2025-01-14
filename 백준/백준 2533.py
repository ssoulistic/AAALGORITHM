input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
graph=[[] for _ in range(N)]
for _ in range(N-1):
    u,v=map(int,input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)
visited=[False for _ in range(N)]
dp=[[1,0] for _ in range(N)]
def dfs(num):
    visited[num]=True
    for next_num in graph[num]:
        if not visited[next_num]:
            acc=dfs(next_num)
            dp[num][0]+=min(acc)
            dp[num][1]+=acc[0]
    return dp[num]
dfs(0)
print(min(dp[0]))
