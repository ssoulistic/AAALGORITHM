input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
L,R=map(int,input().split())
if L+R==2 or L+R==0:
    print("Invalid")
elif L==1:
    print("Yes")
else:
    print("No")
