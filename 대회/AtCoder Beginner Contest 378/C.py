input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))
dict={}
answer=[]
for i in range(N):
    if dict.get(A[i]):
        answer.append(dict[A[i]])
    else:
        answer.append(-1)
    dict[A[i]]=i+1
    
    
print(*answer)
    
    