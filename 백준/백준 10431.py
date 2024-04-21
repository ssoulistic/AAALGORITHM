input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
P=int(input())
for _ in range(P):
    num,*students=map(int,input().split())
    result=0
    queue=[]
    for st in students:
        temp=0
        for q in queue:
            if q>st:
                temp+=1
        queue.append(st)
        result+=temp
    print(num,result)