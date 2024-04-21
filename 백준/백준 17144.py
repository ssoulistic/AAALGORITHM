input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
from collections import deque
R,C,T=map(int,input().split())
room=[]
for _ in range(R):
    room.append(list(map(int,input().split())))

cleaner=[]
for q in range(R):
    if room[q][0]==-1:
        cleaner.append([q,0])
        
for _ in range(T):
    # 1. 미세먼지 확산(동시)
    dust=[[0 for _ in range(C)] for _ in range(R)]
    for ri in range(R):
        for ci in range(C):
            if room[ri][ci]>0:
                for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
                    nr=ri+dr
                    nc=ci+dc
                    if 0<=nr<R and 0<=nc<C and room[nr][nc]!=-1:
                        dust[nr][nc]+=room[ri][ci]//5
                        dust[ri][ci]-=room[ri][ci]//5
    # 1-1. 적용
    for i in range(R):
        for j in range(C):
            room[i][j]+=dust[i][j]

    # 2. 공기청정 구역 이동 들어오는 방향 순
    # 2-1. 윗부분
    c_clockwise=[[0,1],[-1,0],[0,-1],[1,0]]
    wind=deque([0])
    xr,xc=cleaner[0]
    direction=0
    queue=deque([[xr,xc]])
    while queue and direction<4:
        xr,xc=queue.popleft()
        xr+=c_clockwise[direction][0]
        xc+=c_clockwise[direction][1]
        if 0<=xr<R and 0<=xc<C:
            wind.append(room[xr][xc])
            if room[xr][xc]!=-1:
                room[xr][xc]=wind.popleft()
                queue.append([xr,xc])
            else:
                wind.popleft()
        else:
            xr-=c_clockwise[direction][0]
            xc-=c_clockwise[direction][1]
            direction+=1
            queue.append([xr,xc])
    # 2-2. 아랫부분
    c_clockwise=[[0,1],[1,0],[0,-1],[-1,0]]
    wind=deque([0])
    xr,xc=cleaner[1]
    direction=0
    queue=deque([[xr,xc]])
    while queue and direction<4:
        xr,xc=queue.popleft()
        xr+=c_clockwise[direction][0]
        xc+=c_clockwise[direction][1]
        if 0<=xr<R and 0<=xc<C:
            wind.append(room[xr][xc])
            if room[xr][xc]!=-1:
                room[xr][xc]=wind.popleft()
                queue.append([xr,xc])
            else:
                wind.popleft()
        else:
            xr-=c_clockwise[direction][0]
            xc-=c_clockwise[direction][1]
            direction+=1
            queue.append([xr,xc])

    # 3. T초 반복후 남은 미세먼지 출력

answer=0
for rr in room:
    answer+=sum(rr)
print(answer+2)