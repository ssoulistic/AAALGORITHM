input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
T=int(input())
n=int(input())
A=list(map(int,input().split()))
m=int(input())
B=list(map(int,input().split()))
SA=[0]
SB=[0]
X={}
Y={}
for i in range(n):
    SA.append(SA[-1]+A[i])
for i in range(m):
    SB.append(SB[-1]+B[i])
answer=0

for j in range(len(SA)):
    for k in range(j+1,len(SA)):
        if X.get(SA[k]-SA[j]):
            X[SA[k]-SA[j]]+=1
        else:
            X[SA[k]-SA[j]]=1

for j in range(len(SB)):
    for k in range(j+1,len(SB)):
        if Y.get(SB[k]-SB[j]):
            Y[SB[k]-SB[j]]+=1
        else:
            Y[SB[k]-SB[j]]=1
for p,pVal in X.items():
    if Y.get(T-p):
        answer+=pVal*Y[T-p]
print(answer)