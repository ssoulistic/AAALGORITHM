input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N,M=map(int,input().split())
graph=[]
visited=[[0 for _ in range(M)] for _ in range(N)]
direction={"L":[0,-1],"R":[0,1],"U":[-1,0],"D":[1,0]}
for _ in range(N):
    graph.append(list(*input().split()))
    
def search(row,col,idx): #고유index,위치
    if visited[row][col]!=0:
        return 0
    # 지도 밖으로 나가는 방향의 입력은 주어지지 않음.
    while visited[row][col]==0:
        visited[row][col]=idx
        dr,dc=direction[graph[row][col]]
        row+=dr
        col+=dc
    if visited[row][col]==idx:
        return 1
    else:
        return 0
answer=0
for r in range(N):
    for c in range(M):
        answer+=search(r,c,M*r+c+1)
print(answer)
        