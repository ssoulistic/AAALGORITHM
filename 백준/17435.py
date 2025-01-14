input=open("sample.txt","r").readline
# import sys
# input=sys.stdin.readline
import math
m=int(input())
fx=list(map(int,input().split()))
limit=int(math.log2(500000))+1
sparse_table=[[-1 for _ in range(limit)] for _ in range(m)]
for i in range(m):
    sparse_table[i][0]=fx[i]

for j in range(1,limit):
    for i in range(m):
        sparse_table[i][j]=sparse_table[sparse_table[i][j-1]-1][j-1]
Q=int(input())
for _ in range(Q):
    n,x=map(int,input().split())
    while n>0:
        k=int(math.log2(n))
        x=sparse_table[x-1][k]
        n-=2**k
    print(x)
