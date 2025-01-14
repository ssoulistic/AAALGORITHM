input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline 

T=int(input())
def dfs(cur):
    global answer
    current_list=list()
    while True:
        if visited[cur]:
            if cur in current_list:
                answer-=(len(current_list)-current_list.index(cur))
            return 
        current_list.append(cur)
        visited[cur]=True
        cur=sel[cur]

for _ in range(T):
    n=int(input())
    answer=n
    sel=[0]
    sel+=list(map(int,input().split()))
    visited=[False]*(n+1)
    for k in range(1,n+1):
        dfs(k)
    print(answer)