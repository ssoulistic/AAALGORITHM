input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N,K,P,X=map(int,input().split())
# N 층 수 K 디스플레이의 자리수 P 최대 반전수 X 실제 층 수

# 위=> 아래 => 좌=>우 
digit={0:0b1110111,1:0b0010010,2:0b1011101,3:0b1011011,4:0b0111010,
       5:0b1101011,6:0b1101111,7:0b1010010,8:0b1111111,9:0b1111011}

change=[]
for i in range(10):
    temp=[]
    for j in range(10):
        temp.append(bin(digit[i]^digit[j]).count("1"))
    change.append(temp)
# 35 에서 변할 수 있는 수.
# 각 자리에서 경우의수 - 0000인 경우, 합이 넘지않도록.
# K자리수 => 0050 이런식일수도 있음.
# 1. 자리수 맞추기
X="0"*(K-len(str(X)))+str(X)
# 2. 백트래킹을 통해 모두 시도하기? 시간이 될지?
# 자신 제외
answer=0
def backt(num,count,depth):
    global answer
    if  count>P:
        return
    if depth==0:
        if 0<int("".join(num))<=N:
            answer+=1
        return
    for q in range(9,-1,-1):
        backt(num[:depth-1]+[str(q)]+num[depth:],count+change[int(num[depth-1])][q],depth-1)
backt(list(X),0,K)
print(answer-1)