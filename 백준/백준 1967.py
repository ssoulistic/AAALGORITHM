input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
from collections import deque
# dfs 두번을 통해 가장 긴 길이..?
# 하나의 leaf => leaf =>leaf
n=int(input())
graph=[[] for _ in range(n)]
for _ in range(n-1):
    s,e,c=map(int,input().split())
    graph[s-1].append([e-1,c])
    graph[e-1].append([s-1,c])
# 마지막 leaf에서 출발
last=n-1
# 한 좌표에서 다른 좌표로의 이동.
def bfs(start):
    visited=[None]*n
    visited[start]=0
    print(visited)
    queue=deque()
    queue.append([start,0])
    while queue:
        next,acc=queue.popleft()
        for destination,cost in graph[next]:
            if visited[destination]==None:
                visited[destination]=acc+cost
                queue.append([destination,acc+cost])
    answer=[0,-1]
    for v in range(n):
        if visited[v]>answer[0]:
            answer=[visited[v],v]
    return answer
print(bfs(bfs(last)[1])[0])