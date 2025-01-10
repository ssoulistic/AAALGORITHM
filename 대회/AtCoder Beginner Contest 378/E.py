input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline


N,M=map(int,input().split())
A=list(map(int,input().split()))
psA=[0]
answer=0
for i in range(N):
    psA.append(psA[-1]+A[i])
for j in range(N+1):
    for k in range(j+1,N+1):
        answer+=(psA[k]-psA[j])%M
print(answer)