# 시간: 보석과 가방이 최대 30만개씩 => 최악의 경우 450초
# IDEA : 작은 크기의 가방에 대해 그 무게보다 작은 보석들을 모아두고 그중 가장 가치가 큰 보석을 계속 넣기.

input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline

from heapq import *
N,K=map(int,input().split())
jewels=[]
for _ in range(N):
    M,V=map(int,input().split())
    jewels.append([M,V])

bags=[]
for _ in range(K):
    C=int(input())
    bags.append(C)

bags.sort()
jewels.sort()
answer=0
cand=[]

for bag in bags:
    while jewels and jewels[0][0]<=bag:
        heappush(cand,-jewels[0][1])
        heappop(jewels)
    if cand:
        answer-=heappop(cand)
print(answer)