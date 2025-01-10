from collections import deque
input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N,M=map(int,input().split())
do=deque()
su=deque()
for _ in range(N):
    d,s=map(int,input().split())
    do.append(d)
    su.append(s)

    