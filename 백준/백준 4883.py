input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline 
test=1
while True:
    N=input().strip()
    if N=="0":
        break
    N=int(N)
    dp=[[0,0,0] for _ in range(N)]
    graph=[]
    for _ in range(N):
        graph.append(list(map(int,input().split())))

    for k in range(3):
        dp[0][k]=graph[0][k]
    dp[1][0]=dp[0][1]+graph[1][0]
    
    if graph[0][2]<0: 
        dp[0][2]=dp[0][1]+graph[0][2]
        dp[1][1]=min(dp[1][0],dp[0][1],dp[0][2])+graph[1][1]
        dp[1][2]=min(dp[0][1],dp[1][1],dp[0][2])+graph[1][2]
    else:
        dp[1][1]=min(dp[1][0],dp[0][1])+graph[1][1]
        dp[1][2]=min(dp[0][1],dp[1][1])+graph[1][2]
    for row in range(1,N-1):
        dp[row+1][0]=min(dp[row][0],dp[row][1])+graph[row+1][0]
        dp[row+1][1]=min(dp[row][0],dp[row][1],dp[row][2],dp[row+1][0])+graph[row+1][1]
        dp[row+1][2]=min(dp[row][1],dp[row][2],dp[row+1][1])+graph[row+1][2]
    print(*graph,sep="\n")
    print()
    print(*dp,sep="\n")
    print(f"{test}. {dp[N-1][1]}")
    test+=1
