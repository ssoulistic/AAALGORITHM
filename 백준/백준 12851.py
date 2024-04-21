input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
from collections import deque
N,K=map(int,input().split())
graph=[0 for _ in range(2*(N+K))]
count=0
def bfs(start):
    global count
    queue=deque()
    queue.append(start)
    while queue:
        next=queue.popleft()
        if next==K:
            count+=1
            continue
        for func in [lambda x: x-1, lambda x: x+1, lambda x: 2*x]:
            next_num=func(next)
            if 0<=next_num<len(graph):
                if graph[next_num]>=graph[next]+1 or graph[next_num]==0:
                    graph[next_num]=graph[next]+1
                    queue.append(next_num)
                
bfs(N)
print(graph[K])
print(count)