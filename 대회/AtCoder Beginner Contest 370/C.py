input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
S=list(input().strip())
T=list(input().strip())
X=[]
length=len(S)
for i in range(length):
    if S[i]>T[i]:
        S[i]=T[i]
        X.append("".join(S))
for i in range(length-1,-1,-1):
    if S[i]<T[i]:
        S[i]=T[i]
        X.append("".join(S))
print(len(X))
print(*X,sep="\n")