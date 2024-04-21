input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
graph=[]
# 하나를 뽑게 된다면, 이어 뽑는 것들이 모두 포함되어있는 집합 찾기.
group=[False for _ in range(N)]
answer=set()
for _ in range(N):
    graph.append(int(input()))

def dfs(A,B,num):
    if group[num-1]:
        return
    if A==B!=set():
        for i in A:
            group[i-1]=True
            answer.add(i)
    
    if num not in A:
        A.add(num)
        B.add(graph[num-1])
        return dfs(A,B,graph[num-1])
    return
for i in range(N):
    dfs(set(),set(),i+1)
print(len(answer))
for ans in sorted(answer):
    print(ans)
