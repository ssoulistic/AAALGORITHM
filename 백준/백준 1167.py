input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
n=int(input())
from collections import deque
graph=[[] for _ in range(n)]
for _ in range(n):
    start,*ends,z=map(int,input().split())
    for end,cost in zip(ends[0::2],ends[1::2]):
        graph[start-1].append([end-1,cost])

def bfs(start):
    visited=[None]*n
    visited[start]=0
    maxi=[0,None]
    queue=deque()
    queue.append(start)
    while queue:
        next=queue.popleft()
        for destination,costs in graph[next]:
            if visited[destination]==None:
                visited[destination]=visited[next]+costs
                queue.append(destination)
                if visited[destination]>maxi[0]:
                    maxi=[visited[destination],destination]
    return maxi
print(bfs(bfs(n-1)[1])[0])
    
            
    