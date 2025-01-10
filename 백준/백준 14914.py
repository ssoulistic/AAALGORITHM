input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
a,b=map(int,input().split())

for i in range(min(a,b)):
    if a%(i+1)==0 and b%(i+1)==0:
        print(i+1,a//(i+1),b//(i+1))