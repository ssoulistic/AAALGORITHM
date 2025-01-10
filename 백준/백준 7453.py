input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline

A,B,C,D=[],[],[],[]
N=int(input())
for _ in range(N):
    a,b,c,d=map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
    
S1_count=dict()
for a in A:
    for b in B:
        acc=a+b
        if S1_count.get(acc):
            S1_count[acc]+=1
        else:
            S1_count[acc]=1
answer=0   
for c in C:
    for d in D:
        acc=c+d
        if S1_count.get(-acc):
            answer+=S1_count[-acc]
        
print(answer)