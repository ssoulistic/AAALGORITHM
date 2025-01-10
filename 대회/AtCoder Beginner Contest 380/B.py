input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
S=input().strip()
A=list(map(lambda x: len(x),S.split("|")))
print(*A[1:-1])