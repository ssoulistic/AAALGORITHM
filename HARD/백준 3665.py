input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
from collections import deque
T=int(input())
for _ in range(T):
    n=int(input())
    t=list(map(int,input().split()))
    rank={}
    graph=[[] for _ in range(n)]
    indegree=[0 for _ in range(n)]
    # 팀 번호:작년 순위
    for i in range(n):
        rank[t[i]]=i
        
    for i in range(n):
        for j in range(i+1,n):
            graph[i].append(j)
            indegree[j]+=1

    m=int(input())
    for _ in range(m):
        a,b=map(int,input().split())
        if rank[a]<rank[b]:
            graph[rank[b]].append(rank[a])
            graph[rank[a]].remove(rank[b])
            indegree[rank[a]]+=1
            indegree[rank[b]]-=1
        else:
            graph[rank[a]].append(rank[b])
            graph[rank[b]].remove(rank[a])
            indegree[rank[b]]+=1
            indegree[rank[a]]-=1

    queue=deque()
    for j in range(n):
        if indegree[j]==0:
            queue.append(j)
    Flag=False
    answer=[]
    while queue:
        if len(queue)>1:
            Flag=True
            break
        next=queue.popleft()
        answer.append(t[next])
        for k in graph[next]:
            indegree[k]-=1
            if indegree[k]==0:
                queue.append(k)
    
    if len(answer)!=n or Flag:
        print("IMPOSSIBLE")
    else:
        print(*answer)