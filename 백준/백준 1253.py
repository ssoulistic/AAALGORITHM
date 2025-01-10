input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))

dic={}
counting={}
for i in range(N):
    if counting.get(A[i]):
        counting[A[i]]+=1
    else:
        counting[A[i]]=1
    
    for j in range(i+1,N):
        if A[i]!=0 and A[j]!=0:
            dic[A[i]+A[j]]=True
        
answer=0
for p in range(N):
    if counting.get(0):
        # 0이 1개 => 각 숫자가 2개이상이면 ok, 0은 어차피 안나옴.
        if counting[0]==1 and counting[A[p]]>=2:
            dic[A[p]]=True
        # 0이 2개 => 각 숫자가 2개이상, 0끼리 되는 경우 -1
        elif counting[0]==2 and A[p]!=0 and counting[A[p]]>=2:
            dic[A[p]]=True
        # 0이 3개이상 => 각 숫자가 2개이상.
        elif counting[0]>=3 and counting[A[p]]>=2:
            dic[A[p]]=True

for k in range(N):
    if dic.get(A[k]):
        answer+=1
print(answer)
