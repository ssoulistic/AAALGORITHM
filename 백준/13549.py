input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
from collections import deque
N,K=map(int,input().split())
visited=[0]*(100001)
def teleport(coord):
    temp=[]
    while 0<=coord<=50000:
        if visited[2*coord]>visited[coord]:
            visited[2*coord]=visited[coord]
        elif visited[2*coord]==0:
            visited[2*coord]=visited[coord]
        else:
            break
        if K<coord:
             break
        coord*=2
        temp.append(coord)
    return temp

def bfs(coord):
    visited[coord]=1
    que=deque()
    que.append(coord)
    while que:
        next=que.popleft()
        que.extend(teleport(next))
        if next==K or visited[K]:
            return visited[K]
        for i in range(2):
            if i==0:
                nx=next+1
            elif i==1:
                nx=next-1
            if 0<=nx<=1e5:
                if not visited[nx]:
                    visited[nx]=visited[next]+1
                    que.append(nx)
    return visited[K]
print(bfs(N)-1)
    