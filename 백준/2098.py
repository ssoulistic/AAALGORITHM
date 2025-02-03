input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))
print(graph)

dp=[[1e9 for _ in range(N)] for _ in range(1<<N)] # 누적 / 마지막 도착점 

acc=[[] for _ in range(N)]
for bit in range(1<<N):
    for i in range(N):
        if bit & (1<<N-1):
            
    acc
    if bit & 1<<acc
        

for i in range(N):
    1<<i
