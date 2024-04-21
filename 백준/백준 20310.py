input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
S=input().strip()
N=len(S)
zeros=S.count("0")
ones=N-zeros
zeros//=2
ones//=2
# 0은 뒤에서 부터 1은 앞에서부터 지우기
exist=list(S)
i=0
while ones:
    if exist[i]=="1":
        exist[i]=""
        ones-=1
    i+=1
j=N-1
while zeros:
    if exist[j]=="0":
        exist[j]=""
        zeros-=1
    j-=1
print("".join(exist))
    
    
    