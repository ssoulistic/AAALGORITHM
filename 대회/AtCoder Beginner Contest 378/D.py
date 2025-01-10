input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
H,W,K=map(int,input().split())
graph=[]
visited=[[False for _ in range(W)] for _ in range(H)]
count=0
for _ in range(H):
    graph.append(list(input().strip()))
    
for r in range(H):
    for c in range(W):
        if graph[r][c]=="#":
            visited[r][c]=True
            
def dfs(coord,visit_map,moved):
    global count
    if moved==K:
        count+=1
        return
    ri,ci=coord
    
    for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr=ri+dr
        nc=ci+dc
        if 0<=nr<H and 0<=nc<W and not visit_map[nr][nc] and graph[nr][nc]==".":
            visit_map[nr][nc]=True
            dfs([nr,nc],visit_map,moved+1)
            visit_map[nr][nc]=False
    return
            
    
for r in range(H):
    for c in range(W):
        if graph[r][c]==".":
            visited[r][c]=True
            dfs([r,c],visited,0)
            visited[r][c]=False
print(count)
    