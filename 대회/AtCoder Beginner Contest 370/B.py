input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))
start=1
for i in range(1,N+1):
    start=graph[max(start-1,i-1)][min(start-1,i-1)]
print(start)