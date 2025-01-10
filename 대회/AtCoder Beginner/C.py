input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
N=int(input())
G=[[] for _ in range(N)]
H=[[] for _ in range(N)]
MG=int(input())
for _ in range(MG):
    u,v=map(int,input().split())
MH=int(input())
for _ in range(MH):
    a,b=map(int,input().split())
A=[[0 for _ in range(N)] for _ in range(N)]
for i in range(N-1):
    j=1
    for cost in map(int,input().split()):
        A[i][i+j]=cost
        j+=1
print(*A,sep="\n")
    