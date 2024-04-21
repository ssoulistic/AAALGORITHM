input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
n=int(input())
answer=0
stack=[]
for _ in range(n):
    x,y=map(int,input().split())
    build2=set()
    while stack and stack[-1]>y:
        build2.add(stack.pop())
    answer+=len(build2)
    if y:
        stack.append(y)

if stack:
    print(len(set(stack))+answer)
else:
    print(answer)
    
    