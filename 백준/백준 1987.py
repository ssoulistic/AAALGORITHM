input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
from collections import deque
R,C=map(int,input().split())
graph=[]
answer=0
visited=[[set() for _ in range(C)] for _ in range(R)]
for _ in range(R):
    graph.append(list(input().strip()))
def bfs(start):
    global answer
    r,c=start
    history=deque()
    history.append([[r,c],graph[r][c]])
    visited[r][c].add(graph[r][c])
    search=[[-1,0],[1,0],[0,-1],[0,1]]
    while history:
        [ri,ci],string=history.popleft()
        if len(string)>answer:
            answer=len(string)
        for dr,dc in search:
            nr=ri+dr
            nc=ci+dc
            if 0<=nr<R and 0<=nc<C and graph[nr][nc] not in string:
                next_string=string+graph[nr][nc]
                if next_string not in visited[nr][nc]:
                    visited[nr][nc].add(next_string)
                    history.append([[nr,nc],next_string])
    
bfs([0,0])
print(answer)