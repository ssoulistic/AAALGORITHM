input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
graph=[]

for _ in range(N):
    graph.append(list(input().strip()))
graph2=[['' for _ in range(N)] for _ in range(N)]
for r in range(N):
    for c in range(N):
        rotate=min(r,c,N-1-r,N-1-c)
        if rotate % 4 == 0:
            graph2[r][c]=graph[c][N-1-r]
        elif rotate % 4 == 1:
            graph2[r][c]=graph[N-1-r][N-1-c]
        elif rotate % 4 == 2:
            graph2[r][c]=graph[N-1-c][r]
        elif rotate % 4 == 3:
            graph2[r][c]=graph[r][c]

print(*map("".join,graph2),sep="\n")