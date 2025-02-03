input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
from math import log2
from collections import deque
N=int(input())
limit=int(log2(N))+1
graph=[[] for _ in range(N)]
depth=[0 for _ in range(N)]
spt=[[-1 for _ in range(limit)] for _ in range(N)]
weight=[[0 for _ in range(limit)] for _ in range(N)]
for _ in range(N-1):
    u,v,w=map(int,input().split())
    graph[u-1].append([v-1,w])
    graph[v-1].append([u-1,w])

queue=deque([0])
depth[0]=1
while queue:
    curr=queue.popleft()
    for next_node,dist in graph[curr]:
        if not depth[next_node]:
            spt[next_node][0]=curr
            weight[next_node][0]=dist
            depth[next_node]=depth[curr]+1
            
            i=0
            parent=curr
            while spt[parent][i]!=-1 and i<limit:
                spt[next_node][i+1]=spt[parent][i]
                weight[next_node][i+1]=weight[next_node][i]+weight[parent][i]
                parent=spt[parent][i]
                i+=1

            queue.append(next_node)

def lca(u,v):
    # 1. depth를 같게
    acc=0
    if depth[u]<depth[v]:
        u,v=v,u
    # u가 항상 더 크게.
    u,acc=find_anc(u,acc,depth[u]-depth[v])
    
    # 2. lca를 구하면서 비용 누적시키기
    while u!=v:
        for i in range(int(log2(depth[u])),-1,-1):
            if spt[u][i]!=spt[v][i]:
                break
        
        acc+=weight[u][i]
        u=spt[u][i]
        acc+=weight[v][i]
        v=spt[v][i]

    return [u,acc]
    
def find_anc(curr,acc,k):
    # 3. k가 주어질 경우, lca를 구한 후 depth차이들을 이용해서 u나 v에서 k번째거나 k뺸값을 거슬러 올라감.
    while k>0:
        up=int(log2(k))
        acc+=weight[curr][up]
        curr=spt[curr][up]
        k-=2**up

    return [curr,acc]



M=int(input())
# 쿼리 1 u v 경로비용 2 u v k 경로의 k번째 정점   
for _ in range(M):
    n,u,v,*k=map(int,input().split())
    u-=1
    v-=1
    if n==1:
        anc,val=lca(u,v)
        print(val)
    elif n==2:
        k=k[0]-1
        anc,val=lca(u,v)
        if depth[u]-depth[anc]>=k:
            print(find_anc(u,0,k)[0]+1)
        elif depth[u]-depth[anc]<k:
            print(find_anc(v,0,(depth[v]-depth[anc])-(k-(depth[u]-depth[anc])))[0]+1)