input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N,T=map(int,input().split())
p=[0 for _ in range(T+1)]
t=0
for _ in range(N):
    d,m=map(int,input().split())
    t+=m
    for i in range(T,d-1,-1):
        p[i]=max(p[i-d]+m,p[i])
print(max(t-p[-1],0))