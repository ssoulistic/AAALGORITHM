input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N,M=map(int,input().split())
queue=[]
def find(x):
    if group[x]!=x:
        group[x]=find(group[x])
    return group[x]
def union(a,b):
    a,b=find(a),find(b)
    if a!=b:
        group[max(a,b)]=min(a,b)
        return True
    return False

for _ in range(M):
    A,B,C=map(int,input().split())
    queue.append([C,[A,B]])
group=[i for i in range(N)]
queue.sort(reverse=True)

answer=0
max_cost=0
while queue:
    cost,[start,end]=queue.pop()
    if union(start-1,end-1):
        answer+=cost
        max_cost=max(cost,max_cost)
print(answer-max_cost)