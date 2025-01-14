input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline 

N=int(input())
M=int(input())
dp=[0 for _ in range(N+1)]
dp[0]=1
dp[1]=1
for i in range(N-1):
    dp[i+2]=dp[i+1]+dp[i]
start=1
end=0
answer=1
for _ in range(M):
    end=int(input())
    answer*=dp[(end-start)]
    start=end+1
answer*=dp[N-end]
print(answer)
