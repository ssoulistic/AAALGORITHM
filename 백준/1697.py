input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
from collections import deque
N,K=map(int,input().split())
maximum=max(N,K)
visited=[0 for _ in range(2*maximum+1)]
search=["-1","+1","*2"]
def bfs(coord):
    visited[coord]=1
    que=deque()
    que.append(coord)
    while que:
        next=que.popleft()
        if next==K:
            return visited[K]
        for s in search:
            nx=eval(str(next)+s)
            if 0<=nx<=2*maximum:
                if visited[nx]>visited[next]+1 or visited[nx]==0:
                    visited[nx]=visited[next]+1
                    que.append(nx)
    return 
print(bfs(N)-1)