input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
dp1=[[0,0,0] for _ in range(N)]
dp2=[[0,0,0] for _ in range(N)]
dp3=[[0,0,0] for _ in range(N)]
R,G,B=map(int,input().split())
dp1[0]=[R,float("inf"),float("inf")]
dp2[0]=[float("inf"),G,float("inf")]
dp3[0]=[float("inf"),float("inf"),B]

def update(dp,r,g,b,j):
    dp[j][0]=min(dp[j-1][1],dp[j-1][2])+r
    dp[j][1]=min(dp[j-1][0],dp[j-1][2])+g
    dp[j][2]=min(dp[j-1][0],dp[j-1][1])+b

for i in range(1,N):
    R,G,B=map(int,input().split())
    update(dp1,R,G,B,i)
    update(dp2,R,G,B,i)
    update(dp3,R,G,B,i)

dp1[N-1][0]=float("inf")
dp2[N-1][1]=float("inf")
dp3[N-1][2]=float("inf")
print(min(*dp1[N-1],*dp2[N-1],*dp3[N-1]))
