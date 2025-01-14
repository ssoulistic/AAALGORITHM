input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
seq=list(map(int,input().split()))
dp=[1 for _ in range(N)]
for i in range(N):
    for j in range(i+1,N):
        if seq[i]<seq[j]:
            dp[j]=max(dp[j],dp[i]+1)
k=0
maxi=0
count=1
answer=[]
while k<N:
    if dp[k]==count:
        answer.append(seq[k])
        count+=1
    if maxi<dp[k]:
        maxi=dp[k]
    k+=1
print(maxi)
print(*answer)