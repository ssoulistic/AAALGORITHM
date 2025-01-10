input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
command=list(map(int,input().split()))
dp=[{} for _ in range(len(command))]
power={0:[2,2,2,2],1:[1,3,4,3],2:[3,1,3,4],3:[4,3,1,3],4:[3,4,3,1]}
def dfs(kth,ft1,ft2):
    if command[kth]==0:
        return 0
    if dp[kth].get((ft1,ft2)):
        return dp[kth][(ft1,ft2)]
    dp[kth][(ft1,ft2)]=min(dfs(kth+1,command[kth],ft2)+power[ft1][command[kth]-1],dfs(kth+1,ft1,command[kth])+power[ft2][command[kth]-1])
    return dp[kth][(ft1,ft2)]
dfs(0,0,0)
print(dp[0][(0,0)])