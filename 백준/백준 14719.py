input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline

H,W=map(int,input().split())
blocks=list(map(int,input().split()))
answer=0
# 시작 => 자기보다 크거나 같은게 나올때까지 탐색
# 나오면 => 그 곳 부터 또 다시 시작
# 안나오면 => 그것보다 1 작은 수로 다시 시도.
i=0
adj=0
while i<W-1:
    acc=0
    for j in range(i+1,W):
        if blocks[i]+adj<=blocks[j]:
            answer+=(blocks[i]+adj)*(j-i-1)-acc
            adj=0
            i=j
            break
        acc+=blocks[j]
    if j==W-1:
        adj-=1
print(answer)