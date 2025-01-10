input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=input().strip()
if N.count("1")==1 and N.count("2")==2 and N.count("3")==3:
    print("Yes")
else:
    print("No")
