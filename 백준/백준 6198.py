input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline 
N=int(input())
stack=[]
answer=0
for idx in range(N):
    x=int(input())
    while stack and stack[-1][1]<=x:
        idy,y=stack.pop()
        answer+=idx-idy-1
    stack.append([idx,x])

while stack:
    idq,q=stack.pop()
    answer+=idx-idq
print(answer)