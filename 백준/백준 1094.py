input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
X=int(input())
count=0
while X>0:
    count += (X & 1)
    X>>=1
print(count)
    

