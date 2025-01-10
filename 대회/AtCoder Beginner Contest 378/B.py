input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
schedule={}
N=int(input())
for i in range(N):
    q,r=map(int,input().split())
    schedule[i+1]=[q,r]
Q=int(input())
for _ in range(Q):
    t,d=map(int,input().split())
    q,r=schedule[t]
    print(q*((d-1-r)//q+1)+r)
