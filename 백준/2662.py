input=open("sample.txt","r").readline
# import sys
# input=sys.stdin.readline
N,M=map(int,input().split())
profit=[[0 for _ in range(M)]]
for _ in range(N):
    cost,*enp=map(int,input().split())
    profit.append(enp)
print(profit)
track=[[[] for _ in range(M+1)] for _ in range(N+1)]
for i in range(M+1):
    track[0][i]=[0]
for i in range(N+1):
    track[i][0]=[0]
dp=[[0 for _ in range(M+1)] for _ in range(N+1)]
for ent_idx in range(1,M+1):
    for invest in range(N+1):
        for last_invest in range(invest+1):
            if dp[invest][ent_idx]<dp[last_invest][ent_idx-1]+profit[invest-last_invest][ent_idx-1]:
                dp[invest][ent_idx]=dp[last_invest][ent_idx-1]+profit[invest-last_invest][ent_idx-1]
                if ent_idx>1:
                    track[invest][ent_idx]=track[last_invest][ent_idx-1]+[invest-last_invest]
                else:
                    track[invest][ent_idx]=[invest-last_invest]
print(*dp,sep="\n")
print(dp[-1][-1])
print(*track[-1][-1])
print(*track,sep="\n")