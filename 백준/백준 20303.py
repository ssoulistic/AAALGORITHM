input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N,M,K=map(int,input().split())
candies=list(map(int,input().split()))
rel=[i for i in range(N)]
def find(x):
    if rel[x]!=x:
        rel[x]=find(rel[x])
    return rel[x]
    
def union(p,q):
    p=find(p)
    q=find(q)
    if p!=q:
        rel[max(p,q)]=min(p,q)

for _ in range(M):
    a,b=map(int,input().split())
    union(a-1,b-1)
friends={}

for i in range(N):
    x=find(rel[i])
    if friends.get(x):
        friends[x][0]+=1
        friends[x][1]+=candies[i]
    else:
        friends[x]=[1,candies[i]]
fr=list(friends.values())
dp=[[0 for _ in range(len(fr)+1)] for _ in range(K+1)]
for i in range(1,len(fr)+1):
    for limit in range(1,K+1):
        friend,candy=fr[i-1]
        if limit-friend>=0:
            dp[limit][i]=max(dp[limit-friend][i-1]+candy,dp[limit][i-1])
        else:
            dp[limit][i]=dp[limit][i-1]
print(*dp,sep="\n")
print(dp[K-1][-1])