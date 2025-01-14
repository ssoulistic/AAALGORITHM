input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline 
T,W=map(int,input().split())
state=1
dp=[[0 for _ in range(T)] for _ in range(W+1)]
fallen=[]
for i in range(T):
    fall=int(input())
    if fall==1:
        fallen.append(1)
    else:
        fallen.append(0)
# 최대 N번 움직임. => fall 
# dp 로 하면.. 어떻게 하면 좋을지
# N번째에 바뀜 => 
for j in range(T):
    dp[0][j]=sum(fallen[j:])

print()
for p in range(W): # 남은 횟수
    for q in range(T-1): # q 에서 바꿧을때
         # 뒤에 매칭되던 녀석들을 아니도록 처리.
        dp[p+1][q+1]=dp[p+1][q]+(T-q)-dp[p][q+1]
        
print(*dp,sep="\n")

# 논리 세우기
# 움직이지 않은 전 상태에서 바꿧을떄 안바꿧을떄

