input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
T=int(input())
for _ in range(T):
    dic={}
    for i in range(26):
        dic[chr(ord("a")+i)]=[]
    W=input().strip()
    K=int(input())
    mini=len(W)+1
    maxi=-1
    for idx in range(len(W)):
        dic[W[idx]].append(idx)
        if len(dic[W[idx]])>=K:
            length=dic[W[idx]][-1]-dic[W[idx]][-K]+1
            if length<mini:
                mini=length
            if length>maxi:
                maxi=length
    if mini==len(W)+1 and maxi==-1:
        print(-1)
    else:
        print(mini,maxi)