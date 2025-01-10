input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
N,K=map(int,input().split())
cards=list(map(int,input().split()))
print(*cards[N-K:],*cards[:N-K])
