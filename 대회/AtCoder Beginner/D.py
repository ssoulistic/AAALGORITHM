input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
from bisect import *
N=int(input())
X=list(map(int,input().split()))
P=list(map(int,input().split()))
Q=int(input())
prefix_sum=[0]
for i in range(N):
    prefix_sum.append(prefix_sum[-1]+P[i])
for _ in range(Q):
    L,R=map(int,input().split())
    print(prefix_sum[bisect_right(X,R)]-prefix_sum[bisect_left(X,L)])

