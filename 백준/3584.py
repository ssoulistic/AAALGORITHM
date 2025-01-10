input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
T=int(input())
for _ in range(T):
    N=int(input())
    graph=[[] for _ in range(N)]
    depth=[0]*N
    parent=[0]*N
    for _ in range(N):
        A,B=map(int,input().split())
        