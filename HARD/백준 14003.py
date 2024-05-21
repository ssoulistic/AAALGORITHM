input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline  
N=int(input())
A=list(map(int,input().split()))
LIS=[]
memo=[0 for _ in range(N)]

def binsearch(start,end,k):
    if start>=end:
        return end
    mid=(start+end)//2
    if k<=LIS[mid]:
        return binsearch(start,mid,k)
    else:
        return binsearch(mid+1,end,k)

for i in range(N):
    if LIS:
        if LIS[-1]<A[i]:
            LIS.append(A[i])
            memo[i]=len(LIS)-1
        else:
            num=binsearch(0,len(LIS)-1,A[i])
            LIS[num]=A[i]
            memo[i]=num
    else:
        LIS.append(A[i])
        memo[i]=i

longest=len(LIS)
idx=N-1
answer=[]
while longest:
    if memo[idx]==longest-1:
        answer.append(A[idx])
        longest-=1
    idx-=1

print(len(LIS))
print(*answer[::-1])