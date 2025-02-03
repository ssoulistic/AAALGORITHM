input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
V,E=map(int,input().split())
finished=[False for _ in range(V+1)]
graph=[[] for _ in range(V+1)]
parent=[0 for _ in range(V+1)]
for _ in range(E):
    # A->B
    A,B=map(int,input().split())
    graph[A].append(B)

def scc(num,stack):
    global finished
    if parent[num]==num and not finished[num]:
        answer=[]
        while stack and stack[-1]!=num:
            x=stack.pop()
            finished[x]=True
            answer.append(x)

        finished[num]=True
        answer.append(num)
        return answer
    parent[num]=num
    stack.append(num)
    for nx in graph[num]:
        if not finished[nx]:
            return scc(nx,stack)
    
    return []

results=[]
for i in range(1,V+1):
    results.append(sorted(scc(i,[])))
print(*results,sep="\n")
