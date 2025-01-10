input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    answer=0
    triples={}
    mp1={}
    mp2={}
    mp3={}
    for i in range(n-2):
        if (a[i],a[i+1]) not in mp1:
            mp1[(a[i],a[i+1])]=0
        if (a[i+1],a[i+2]) not in mp2:
            mp2[(a[i+1],a[i+2])]=0
        if (a[i],a[i+2]) not in mp3:
            mp3[(a[i],a[i+2])]=0
        if (a[i],a[i+1],a[i+2]) not in triples:
            triples[(a[i],a[i+1],a[i+2])]=0
        
        mp1[(a[i],a[i+1])]+=1
        mp2[(a[i+1],a[i+2])]+=1
        mp3[(a[i],a[i+2])]+=1
        triples[(a[i],a[i+1],a[i+2])]+=1
        
    for j in range(n-2):
        answer+=mp1[(a[j],a[j+1])]-triples[(a[j],a[j+1],a[j+2])]
        answer+=mp2[(a[j+1],a[j+2])]-triples[(a[j],a[j+1],a[j+2])]
        answer+=mp3[(a[j],a[j+2])]-triples[(a[j],a[j+1],a[j+2])]
    print(answer//2)