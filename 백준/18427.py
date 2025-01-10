input=open("sample.txt","r").readline
# import sys
# input=sys.stdin.readline
N,M,H=map(int,input().split())
st=[]
dp = [[0 for _ in range(N+1)] for _ in range(H+1)]
for _ in range(N):
    st.append(list(map(int,input().split())))
for i in range(N+1):
    dp[0][i]=1

for i in range(1,N+1):
    for j in range(H+1):
        dp[j][i]=dp[j][i-1]
        for s in st[i-1]:
            if j>=s:
                dp[j][i]+=dp[j-s][i-1]
print(dp[-1][-1]%10007)