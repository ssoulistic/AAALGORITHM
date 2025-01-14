input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline 
N,K=map(int,input().split())
given=input().strip()
stack=[]
for i in range(N):
    while K>0 and stack and stack[-1]<given[i]:
        stack.pop()
        K-=1
    stack.append(given[i])
while K>0 and stack:
    stack.pop()
    K-=1
if stack:
    print("".join(stack))
else:
    print(0)
        
