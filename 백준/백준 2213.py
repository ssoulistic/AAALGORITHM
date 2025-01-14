input=open("sample.txt",'r').readline
import sys
# input=sys.stdin.readline
sys.setrecursionlimit(10**6)
n=int(input())
w=list(map(int,input().split()))
graph=[set() for _ in range(n)]
visited=[False for _ in range(n)]
dp=[[0,0] for _ in range(n)]
memo=[[[i+1],[]] for i in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a-1].add(b-1)
    graph[b-1].add(a-1)
def dfs(cur_node):
    visited[cur_node]=True
    dp[cur_node][0]=w[cur_node]
    for next_node in graph[cur_node]:
        if not visited[next_node]:
            temp=dfs(next_node)
            memo[cur_node][0].extend(memo[next_node][1])
            dp[cur_node][0]+=temp[1]
            if temp[0]>temp[1]:
                dp[cur_node][1]+=temp[0]
                memo[cur_node][1].extend(memo[next_node][0])
            else:
                dp[cur_node][1]+=temp[1]
                memo[cur_node][1].extend(memo[next_node][1])
    return dp[cur_node]
dfs(0)

if dp[0][0]>dp[0][1]:
    print(dp[0][0])
    print(*sorted(memo[0][0]))
else:
    print(dp[0][1])
    print(*sorted(memo[0][1]))