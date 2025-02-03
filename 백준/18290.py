input=open("sample.txt",'r').readline
import sys
# input=sys.stdin.readline
N,M,K=map(int,input().split())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))
picked=[[False]*M for _ in range(N)]
answer=-1e9

def dfs(i,acc,K):
    global answer
    global picked
    if K==0:
        if answer<acc:
            answer=acc
        return
    if i>=N*M or N*M-i-K<0 or answer>acc+10000*K:
        return
    r,c=divmod(i,M)
    gr=(-1,1,0,0)
    gc=(0,0,-1,1)
    
    dfs(i+1,acc,K)
    if all(not picked[r+g[0]][c+g[1]] if 0<=r+g[0]<N and 0<=c+g[1]<M else True for g in zip(gr,gc)):
        picked[r][c]=True
        dfs(i+1,acc+graph[r][c],K-1)
        picked[r][c]=False
dfs(0,0,K)
print(answer)