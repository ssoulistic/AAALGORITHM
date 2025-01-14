input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline 
N=int(input())
dp=[0 for _ in range(N+1)]
seq=[]
befmax=0
answer=0
for idx in range(N):
    T,P=map(int,input().split())
    start=idx
    end=idx+T
    earn=P
    befmax=max(dp[start],befmax)
    if 0<=end<=N:
        dp[end]=max(dp[end],befmax+earn)
        answer=max(dp[end],answer)
print(answer)