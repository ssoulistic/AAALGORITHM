input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
from heapq import *
N,M=map(int,input().split())
graph=[[] for _ in range(N)]
for _ in range(M):
    A,B,C=map(int,input().split())
    graph[A-1].append([B-1,C])
    graph[B-1].append([A-1,C])

def dijkstra(start):
    feed=[1e9 for _  in range(N)]
    queue=[[0,start]]
    heapify(queue)
    while queue:
        acc,next_destination=heappop(queue)
        if feed[next_destination]<acc:
            continue
        for next,cost in graph[next_destination]:
            if feed[next]>acc+cost:
                feed[next]=acc+cost
                heappush(queue,[acc+cost,next])
    return feed[N-1]
print(dijkstra(0))