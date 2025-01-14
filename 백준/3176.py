
input=open("sample.txt","r").readline
# import sys
# input=sys.stdin.readline

import math
from collections import deque
N=int(input())
graph=[[] for _ in range(N)]
visited=[False for _ in range(N)]
limit=int(math.log2(N))+1
sparse_table=[[[-1,1e9,0] for _ in range(limit)] for _ in range(N)] # 2**ith parent, minimum, maximum
depth=[0 for _ in range(N)]
# root는 1
for _ in range(N-1):
    a,b,dist=map(int,input().split())
    graph[a-1].append([b-1,dist])
    graph[b-1].append([a-1,dist])

queue=deque([0])
sparse_table[0][0]=[-1,1e9,-1e9]
visited[0]=True
while queue:
    node=queue.popleft()
    for next_node,distance in graph[node]:
        if not visited[next_node]:
            parent_node=node
            sparse_table[next_node][0][0]=parent_node
            sparse_table[next_node][0][1]=min(sparse_table[next_node][0][1],distance)
            sparse_table[next_node][0][2]=max(sparse_table[next_node][0][2],distance)
            i=0
            # 부모의 1번째 = 자식의 2번째, 부모의 1번째의 2번째 = 자식의 4번째, 부모의 1번째의 2번째 의 4번째 = 자식의 8번째
            while parent_node!=-1 and i+1 < limit:
                sparse_table[next_node][i+1][0]=sparse_table[parent_node][i][0]
                sparse_table[next_node][i+1][1]=min(sparse_table[parent_node][i][1],sparse_table[next_node][i+1][1],sparse_table[next_node][i][1])
                sparse_table[next_node][i+1][2]=max(sparse_table[parent_node][i][2],sparse_table[next_node][i+1][2],sparse_table[next_node][i][2])
                parent_node=sparse_table[parent_node][i][0]
                i+=1
            depth[next_node]=depth[node]+1
            visited[next_node]=True
            queue.append(next_node)

def lca(a,b,minimum,maximum):
    while a!=b:
        for i in range(limit):
            if sparse_table[a][i][0]==sparse_table[b][i][0]:
                break

        if i==0:
            i=1
        minimum=min(minimum,sparse_table[a][i-1][1],sparse_table[b][i-1][1])
        maximum=max(maximum,sparse_table[a][i-1][2],sparse_table[b][i-1][2])
        a=sparse_table[a][i-1][0]
        b=sparse_table[b][i-1][0]

    return [minimum,maximum]


K=int(input())
for _ in range(K):
    d,e=map(int,input().split())
    d-=1
    e-=1

    minimum=1e9
    maximum=0

    # depth 일치
    if depth[d]>depth[e]: # e가 항상 더 크도록. 계산편의
        d,e=e,d
    while depth[d]!=depth[e]:
        diff=int(math.log2(depth[e]-depth[d]))
        minimum=min(minimum,sparse_table[e][diff][1])
        maximum=max(maximum,sparse_table[e][diff][2])
        e=sparse_table[e][diff][0]
    print(*lca(d,e,minimum,maximum))

