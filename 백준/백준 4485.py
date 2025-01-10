input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
from heapq import *
problem_num=0
while True:
    problem_num+=1
    answer=0
    N=int(input())
    if N==0:
        break
    graph=[]
    for _ in range(N):
        graph.append(list(map(int,input().split())))
    queue=[[graph[0][0],[0,0]]]
    heapify(queue)
    search=[[-1,0],[1,0],[0,-1],[0,1]]
    cave=[[N*10 for _ in range(N)] for _ in range(N)]
    while queue:
        acc,[ri,ci]=heappop(queue)
        if cave[ri][ci]<acc:
            continue
        for dr,dc in search:
            nr=ri+dr
            nc=ci+dc
            if 0<=nr<N and 0<=nc<N:
                if cave[nr][nc]>graph[nr][nc]+acc:
                    cave[nr][nc]=graph[nr][nc]+acc
                    heappush(queue,[graph[nr][nc]+acc,[nr,nc]])
    print(f"Problem {problem_num}: {cave[N-1][N-1]}")
    