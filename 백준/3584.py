input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline

class Node(object):
    def __init__(self,parent=None,value=0,depth=0):
        self.parent=parent
        self.value=value
        self.depth=depth
        
class tree(object):
    def __init__(self,number):
        self.leaf=[]
        for i in range(number):
            self.leaf.append(Node(value=i+1))
    
    def insert_info(self,A,B):
        na=self.leaf[A-1]
        nb=self.leaf[B-1]
        nb.parent=na

    def depth(self,x):
        node_x=self.leaf[x]
        count=0
        while node_x.parent!=None or node_x.depth!=0:
            node_x=node_x.parent
            count+=1
        self.leaf[x].depth=node_x.depth+count

    def lca(self,A,B):
        node_a=self.leaf[A-1]
        node_b=self.leaf[B-1]
        self.depth(A-1)
        self.depth(B-1)
        while node_a.depth!=node_b.depth:
            if node_a.depth>node_b.depth:
                node_a=node_a.parent
            else:
                node_b=node_b.parent
        while node_a.value!=node_b.value:
            if node_a.parent:
                node_a=node_a.parent
            if node_b.parent:
                node_b=node_b.parent
        return node_a.value
def main():
  T=int(input())
  for _ in range(T):
      N=int(input())
      inst=tree(N)
      for _ in range(N-1):
          A,B=map(int,input().split())
          inst.insert_info(A,B)
      t1,t2=map(int,input().split())
      print(inst.lca(t1,t2))
main()


# T=int(input())
# for _ in range(T):
#     N=int(input())
#     parent=[0]*N
#     for _ in range(N-1):
#         A,B=map(int,input().split())
#         parent[B-1]=A
#     t1,t2=map(int,input().split())
#     d1,d2=0,0
#     a,b=t1,t2
#     while parent[a-1]!=0:
#         a=parent[a-1]
#         d1+=1
#     while parent[b-1]!=0:
#         b=parent[b-1]
#         d2+=1
    
#     while d1!=d2:
#         if d1>d2:
#             t1=parent[t1-1]
#             d1-=1
#         else:
#             t2=parent[t2-1]
#             d2-=1
    
#     while t1!=t2:
#         t1=parent[t1-1]
#         t2=parent[t2-1]
#     print(t1)        
