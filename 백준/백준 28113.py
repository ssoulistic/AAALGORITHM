input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline

N,A,B=map(int,input().split())
if A<B:
    print("Bus")
elif A>B:
    print("Subway")
else:
    print("Anything")
