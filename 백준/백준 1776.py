input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
from heapq import *
N,M=map(int,input().split())
indegree=[0 for _ in range(N)]
graph=[[] for _ in range(N)]
answer=[]
for _ in range(M):
    A,B=map(int,input().split())
    indegree[B-1]+=1
    graph[A-1].append(B-1)

queue=[]
for i in range(N):
    if indegree[i]==0:
        heappush(queue,i)

answer=[]
while queue:
    next=heappop(queue)
    answer.append(next+1)
    for j in graph[next]:
        indegree[j]-=1
        if indegree[j]==0:
            heappush(queue,j)
print(answer)