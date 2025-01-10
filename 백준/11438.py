input=open("sample.txt","r").readline
# import sys
# input=sys.stdin.readline
from collections import deque
import math
N=int(input())
spt=[[-1 for _ in range(17)] for _ in range(N)]
depth=[0 for _ in range(N)]
graph=[[] for _ in range(N)]
for _ in range(N-1):
    A,B=map(int,input().split())
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)

queue=deque([[0,0]])
while queue:
    curr_node,dth=queue.popleft()
    for next_node in graph[curr_node]:
        if spt[next_node][0]==-1 and next_node!=0: # child
            spt[next_node][0]=curr_node
            depth[next_node]=dth+1
            for i in range(16):
                spt[next_node][i+1]=spt[spt[next_node][i]][i]
            queue.append([next_node,dth+1])

M=int(input())
for _ in range(M):
    t1,t2=map(int,input().split())
    t1-=1
    t2-=1
    
    if depth[t1]>depth[t2]:
        diff=depth[t1]-depth[t2]
        while diff>0:
            p=int(math.log2(diff))
            t1=spt[t1][p]
            diff-=2**p
    elif depth[t1]<depth[t2]:
        diff=depth[t2]-depth[t1]
        while diff>0:
            p=int(math.log2(diff))
            t2=spt[t2][p]
            diff-=2**p
    i=0
    while t1!=t2:
        if spt[t1][i]==spt[t2][i]:
            if i>0:
                t1=spt[t1][i-1]
                t2=spt[t2][i-1]
                i=-1
            else:
                t1=spt[t1][i]
                t2=spt[t2][i]
        i+=1
    print(t1+1)
        