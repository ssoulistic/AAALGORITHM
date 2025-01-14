input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline 
N=int(input())
dp=[0 for _ in range(N)]
seq=[]
for idx in range(N):
    T,P=map(int,input().split())
    seq.append([idx,T,P])

def dfs(day,acc):
    dp[day]=max(dp[day],acc)
    for next in range(day+1,N):
        start,take,earn=seq[next]
        if start+take-1<N:
            dfs(start+take-1,acc+earn)
        else:
            dfs(next,acc)
    return

dfs(0,0)
s,t,e=seq[0]
if s+t-1<N:
    dfs(s+t-1,e)

print(max(dp))