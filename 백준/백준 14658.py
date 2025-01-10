input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline

N,M,L,K=map(int,input().split())
stars=[]
for _ in range(K):
    x,y=map(int,input().split())
    stars.append([x,y])
stars.sort()
answer=0
def dfs(minXY,maxXY,nth,chosen):
    global answer
    if nth==K-1:
        answer=max(chosen,answer)
        return
    minTEMP=minXY
    maxTEMP=maxXY
    minXY=[min(minXY[0],stars[nth][0]),min(minXY[1],stars[nth][1])]
    maxXY=[max(maxXY[0],stars[nth][0]),max(maxXY[1],stars[nth][1])]
   
    if maxXY[0]-minXY[0]>L:
        answer=max(chosen,answer)
        return
    elif maxXY[0]-minXY[0]<=L and maxXY[1]-minXY[1]<=L:
        dfs(minXY,maxXY,nth+1,chosen+1)
    dfs(minTEMP,maxTEMP,nth+1,chosen)
dfs([N+1,M+1],[-1,-1],0,0)
print(K-answer)