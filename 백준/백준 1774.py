input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
from heapq import *
from collections import deque
N,M=map(int,input().split())

def distance(p,q):
    x1,y1=p
    x2,y2=q
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def search(c):
    queue=deque()
    queue.append(c)
    result=[]
    while queue:
        next=queue.popleft()
        connected[next]=True
        result.append(next)
        for n2 in graph[next]:
            if not connected[n2]:
                queue.append(n2)
    return result

def signal(god_line):
    for god in god_line:
        for j in range(N):
            if not connected[j]:
                heappush(star_heap,[distance(gods[god],gods[j]),god,j])

gods=[]
for _ in range(N):
    X,Y=map(int,input().split())
    gods.append([X,Y])
graph=[[] for _ in range(N)]

for _ in range(M):
    a,b=map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

connected=[False]*N
connected[0]=True

star_heap=[]
signal(search(0))
answer=0
while star_heap:
    val,z1,z2=heappop(star_heap)
    if not connected[z2]:
        answer+=val
        connected[z2]=True
        signal(search(z2))
print(f"{round(answer,2):.2f}")
