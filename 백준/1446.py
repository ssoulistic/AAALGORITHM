input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
from heapq import *
N,D=map(int,input().split())
road=[i for i in range(10001)]
command=[]
for _ in range(N):
    s,e,dis=map(int,input().split())
    command.append([s,e,dis])
for s,e,dis in sorted(command):
    road[e]=min(road[e],road[s]+dis)
    for j in range(e-1,D):
        road[j+1]=min(road[j]+1,road[j+1])
print(road[D])