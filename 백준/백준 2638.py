input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
from collections import deque
N,M =map(int,input().split())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))


# 외부공기 접촉
def bfs(start):
    r,c=start
    melt=[]
    visited[r][c]=True
    queue=deque()
    queue.append([r,c])
    while queue:
        ri,ci=queue.popleft()
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr=ri+dr
            nc=ci+dc
            if 0<=nr<N and 0<=nc<M:
                if graph[nr][nc]==0 and not visited[nr][nc]:
                    visited[nr][nc]=True
                    queue.append([nr,nc])
                elif graph[nr][nc]==1:
                    if not visited[nr][nc]:
                        visited[nr][nc]=1
                    elif visited[nr][nc]==1:
                        visited[nr][nc]=2
                        melt.append([nr,nc])
    return melt
    
sec=0
while True:
    visited=[[False for _ in range(M)] for _ in range(N)]
    cheese=bfs([0,0])
    if not cheese:
        break
    for zr,zc in cheese:
        graph[zr][zc]=0
    sec+=1
print(sec)