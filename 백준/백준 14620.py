input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))    
min_cost=float("inf")
visited=[[False for _ in range(N)] for _ in range(N)]
# 3개
def backtrack(row,col,seed_left,cost_acc):
    global min_cost

    if seed_left==0:
        min_cost=min(cost_acc,min_cost)
        return
    if col>=N-1:
        row+=1
        col=1
    if row>=N-1:
        return
    if visited[row][col]:
        backtrack(row,col+1,seed_left,cost_acc)
        return
    
    
    directions=[[-1,0],[1,0],[0,-1],[0,1]]
    land_cost=graph[row][col]
    for dr,dc in directions:
        nr=row+dr
        nc=col+dc
        land_cost+=graph[nr][nc]
        if visited[nr][nc]:
            backtrack(row,col+1,seed_left,cost_acc)
            return
    
    visited[row][col]=True
    for dr,dc in directions:
        nr=row+dr
        nc=col+dc
        visited[nr][nc]=True
    
    backtrack(row,col+1,seed_left-1,cost_acc+land_cost)
        
    visited[row][col]=False
    for dr,dc in directions:
        nr=row+dr
        nc=col+dc
        visited[nr][nc]=False    
    backtrack(row,col+1,seed_left,cost_acc)
    return

backtrack(1,1,3,0)
print(min_cost)