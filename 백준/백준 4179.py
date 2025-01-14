input=open("C:/Users/서호/취업준비/코딩테스트/AAALGORITHM/sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
from collections import deque
R,C=map(int,input().split())
graph=[]
fire=[]
for r in range(R):
    line=list(input().strip())
    for c in range(C):
        if line[c]=="J":
            line[c]="."
            jihoon=[r,c]
        elif line[c]=="F":
            line[c]=0
            fire.append([r,c])
    graph.append(line)
search=[[-1,0],[1,0],[0,-1],[0,1]]
# 불 지도를 만듬 => 불 확산 지도를 따라 이동시키기.
# 불지도 => 최단으로 만드는 법.
def fire_expand(fires):
    queue=deque(fires)
    while queue:
        ri,ci=queue.popleft()
        for dr,dc in search:
            nr=ri+dr
            nc=ci+dc
            if 0<=nr<R and 0<=nc<C and graph[nr][nc]!="#":
                if graph[nr][nc]==".":
                    graph[nr][nc]=graph[ri][ci]+1
                    queue.append([nr,nc])
    return 

def escape(start):
    queue=deque([start])
    rr,cc=start
    visited=[[1e6 for _ in range(C)] for _ in range(R)]
    visited[rr][cc]=0
    answer=1e6
    while queue:
        ri,ci=queue.popleft()
        for dr,dc in search:
            nr=ri+dr
            nc=ci+dc
            if 0<=nr<R and 0<=nc<C and graph[nr][nc]!="#" and visited[nr][nc]==1e6:
                # 불보다 빠르게
                if graph[nr][nc]=="." or graph[nr][nc]>visited[ri][ci]+1:
                    visited[nr][nc]=visited[ri][ci]+1
                    queue.append([nr,nc])
                    if (nr==0 or nr==R-1 or nc==0 or nc==C-1):
                        if answer>visited[ri][ci]+1:
                            answer=visited[ri][ci]+1

    for r in range(R):
        if answer>visited[r][0]:
            answer=visited[r][0]
        if answer>visited[r][C-1]:
            answer=visited[r][C-1]
    for c in range(C):
        if answer>visited[0][c]:
            answer=visited[0][c]
        if answer>visited[R-1][c]:
            answer=visited[R-1][c]
    if answer==1e6:
        return "IMPOSSIBLE"
    else:
        return answer+1
fire_expand(fire)
print(escape(jihoon))