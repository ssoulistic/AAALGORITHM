input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
seq=list(map(int,input().split()))
# 1. 최대한 중복되지 않는 긴 순열 만드는 것이 목표
# 2. 하나씩 더하며, 중복x => 해당 숫자를 포함하며 만들 수 있는 경우의수 더하기
# 3. 중복 o => 중복x까지 앞의값 조정 => 해당 숫자를 포함하여 만들 수 있는 경우의 수 더하기
dic={}
answer=1
s,e=0,0
dic[seq[e]]=e
while s<=e<N-1:
    e+=1
    if dic.get(seq[e])==None:
        answer+=e-s+1
        dic[seq[e]]=e
    else:
        deletion=[]
        for k,v in dic.items():
            if v<dic[seq[e]]:
                deletion.append(k)
        s=dic[seq[e]]+1
        for d in deletion:
            del dic[d]
        answer+=e-s+1
        dic[seq[e]]=e
print(answer)