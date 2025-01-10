input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
enemy=list(map(int,input().split()))
T=0
for e in enemy:
    q,l=divmod(e,5)
    T+=q*3
    e=l
    while e>0:
        T+=1
        if T%3==0:
            e-=3
        else:
            e-=1
print(T)

