input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
tower=list(map(int,input().split()))
stack=[]
answer=[]
for t in range(N):
    if stack:
        if stack[-1][1]>tower[t]:
            answer.append(stack[-1][0])
            stack.append([t+1,tower[t]])
        else:
            while stack and stack[-1][1]<tower[t]:
                stack.pop()
            if stack:
                answer.append(stack[-1][0])
            else:
                answer.append(0)
            stack.append([t+1,tower[t]])
    else:
        answer.append(0)
        stack.append([t+1,tower[t]])
print(*answer)
        
        



