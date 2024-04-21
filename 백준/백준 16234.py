input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
from collections import deque
N,L,R=map(int,input().split())
A=[]
for _ in range(N):
    A.append(list(map(int,input().split())))
# 1. bfs => 연합의 나라 구하기(좌표들) visit으로 모두 체크
#  -> 바로 배분 해버리고, visit으로 접근 못하게 하기.
# 2. 연합의 나라들 => 국민 배분
# 3. 반복
# visited => False => 접근안한 곳
# group_num => 이미 완료된 곳.
def bfs(coord,group_num):
    r,c=coord
    if visited[r][c]:
        return False
    search=[[-1,0],[1,0],[0,-1],[0,1]]
    queue=deque()
    queue.append([r,c])
    alliance=[]
    while queue:
        ri,ci=queue.popleft()
        for dr,dc in search:
            nr=ri+dr
            nc=ci+dc
            if 0<=nr<N and 0<=nc<N:
                if not visited[nr][nc]:
                    if L<=abs(A[nr][nc]-A[ri][ci])<=R:
                        visited[nr][nc]=group_num
                        queue.append([nr,nc])
                        alliance.append([nr,nc])
    return alliance

count=0
while count<2000:
    count+=1
    visited=[[False for _ in range(N)] for _ in range(N)]
    gn=1
    Flag=True
    groups=[]
    for i in range(N):
        for j in range(N):
            check=bfs([i,j],gn)
            if check:
                groups.append(check)
                gn+=1
                Flag=False
    if Flag:
        count-=1
        break
    for group in groups:
        acc=0
        for gr,gc in group:
            acc+=A[gr][gc]
        acc//=len(group)
        for gr,gc in group:
            A[gr][gc]=acc
print(count)
