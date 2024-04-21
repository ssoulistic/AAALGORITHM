input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
n,m,r=map(int,input().split())
floyd=[[1e9 for _ in range(n)] for _ in range(n)]
for p in range(n):
    floyd[p][p]=0
items=list(map(int,input().split()))
for _ in range(r):
    a,b,l=map(int,input().split())
    floyd[a-1][b-1]=l
    floyd[b-1][a-1]=l
for k in range(n):
    for i in range(n):
        for j in range(n):
            if floyd[i][j]>floyd[i][k]+floyd[k][j]:
                floyd[i][j]=floyd[i][k]+floyd[k][j]
answer=0
for area in floyd:
    acc=0
    print(area)
    for a in range(n):
        if area[a]<=m:
            acc+=items[a]
    answer=max(acc,answer)
print(answer)