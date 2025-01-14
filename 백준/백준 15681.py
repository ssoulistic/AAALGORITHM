input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline 
N,R,Q = map(int,input().split())
connect=[[]for _ in range(N)]
tree=[[-1,set()] for _ in range(N)] # parent,child

for _ in range(N-1):
    U,V=map(int,input().split())
    connect[U-1].append(V-1)
    connect[V-1].append(U-1)

def makeTree(currentNode, parent) :
    for node in connect[currentNode]:
        if node !=parent:
            tree[node][0]=currentNode
            tree[currentNode][1].add(node)
            makeTree(node,currentNode)
def countSubtreeNodes(currentNode):
    size[currentNode]=1
    for node in tree[currentNode][1]:
        countSubtreeNodes(node)
        size[currentNode]+=size[node]
makeTree(R-1,-1)
size=[1 for _ in range(N)]
countSubtreeNodes(R-1)
for _ in range(Q):
    U=int(input())
    print(size[U-1])