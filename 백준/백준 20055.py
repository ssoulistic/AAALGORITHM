input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
from collections import deque
# 슬라이딩 윈도우
N,K=map(int,input().split())
belt=list(map(int,input().split()))
zeros=belt.count(0)
robots=deque()
s,e=1,N
level=0
while zeros<K:
    level+=1
    # 1. 회전
    if s==1:
        s=2*N
    else:
        s-=1
    if e==1:
        e=2*N
    else:
        e-=1
    # 즉시 내림.
    if robots and robots[0]==e:
        robots.popleft()
    
    # 2. 로봇이동
    for r in range(len(robots)):
        # s,e 사이에 있을 것이므로
        next=robots[r]+1
        if robots[r]==2*N:
            next=1
        if belt[next-1]>0 and next not in robots:
            belt[next-1]-=1
            if belt[next-1]==0:
                zeros+=1
            robots[r]=next
    
    # 즉시 내림.
    if robots and robots[0]==e:
        robots.popleft()
    
    # 3. 로봇 올리기
    if belt[s-1]>0:
        belt[s-1]-=1
        if belt[s-1]==0:
            zeros+=1
        robots.append(s)
    # 4. 내구도 0이 K개 이상이면 종료
print(level)

