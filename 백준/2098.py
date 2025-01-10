input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))
print(graph)

dp=[[1e9 for _ in range(N)] for _ in range(1<<N)]

for i in range(N):
    dp[1<<i][i]=0
for i in range(1<<N): # 누적 기록
    for j in range(N): # 마지막이 j번째 도시일때, 다른 도시 에서 j번 도시로 올때의 최소값
        for k in range(N):
            if i & 1<<k and k!=j:
                dp[i][j]=min(dp[i][j],dp[i & ~1<<k][k]+graph[k][j] if dp[i & ~1<<k][k]!=1e9 else graph[k][j])
print(*dp,sep="\n")
print(min(dp[-1]))