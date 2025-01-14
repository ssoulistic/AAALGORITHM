input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline 
K=int(input())
for i in range(K):
    h=int(input())
    strings=input().strip()
    for s in strings:
        if s=="c":
            h+=1
        elif s=="b":
            h-=1
    print(f"Data Set {i+1}:")
    print(h)
    print()