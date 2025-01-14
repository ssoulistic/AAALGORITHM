# 좌표평면에서 최단거리란 무엇인가를 생각해보기.

input=open("sample.txt",'r').readline
from heapq import *
# import sys
# input=sys.stdin.readline
N=int(input())
planets=[]
for idx in range(N):
    x,y,z=map(int,input().split())
    planets.append([idx,x,y,z])
tunnels=set()
for k in range(1,4):
    planets.sort(key=lambda x: x[k])
    for i in range(N-1):
        tunnels.add((min(map(lambda x,y: abs(x-y),planets[i][1:],planets[i+1][1:])),planets[i][0],planets[i+1][0]))

cycle=[i for i in range(N)]

def find(x):
    if cycle[x]!=x:
        cycle[x]=find(cycle[x])
    return cycle[x]
def union(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return False
    cycle[max(a,b)]=min(a,b)
    return True
cost=0
for dist,c1,c2 in sorted(tunnels):
    if union(c1,c2):
        cost+=dist
print(cost)