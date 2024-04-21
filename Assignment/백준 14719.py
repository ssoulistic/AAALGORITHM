input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline

H,W=map(int,input().split())
blocks=list(map(int,input().split()))
answer=0
# 증가할 때 => 작은 거 => 왼쪽으로 칸채우기 큰거 => 
# 감소할 떄 => 
highest=[0,0] #idx height
acc=0
for i in range(W):
    if highest[1]<=blocks[i]:
        answer+=min(highest[1],blocks[i])*(i-highest[0]-1)-acc
        acc=0
        highest=[i,blocks[i]]
    elif highest[1]>blocks[i]:
        acc+=blocks[i]
if acc:
    answer+=min(highest[1],blocks[i])*(i-highest[0])-acc
    acc=0
print(answer)