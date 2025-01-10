input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N,M,K=map(int,input().split()) #수의 개수 / 수의 변경 횟수 / 구간의 합
# 2~N+1 N개의 수
seq=[]

class segTree():
    tree_nodes=[0 for _ in range(N+1)]
    def __init__(self) -> None:
        pass
    def update(self,ql,qr,target_node,val,idxl,idxr):
        if idxr<ql or idxl>qr:
            return 0
        if ql==qr==target_node:
            self.tree_nodes[target_node]=val
            return self.tree_nodes[target_node]
        mid = (ql+qr)//2
        self.tree_nodes += self.update(ql,mid,target_node,val,idxl,idxr)+self.update(mid+1,qr,target_node,val,idxl,idxr)
        
    















class segTree():
    tree_nodes=[0 for _ in range(N*4+1)]
    def __init__(self) -> None:
        pass
    def est(self,start,end,index):
        if start==end:
            self.tree_nodes[index]=seq[start]
            return self.tree_nodes[index]
        mid = (start+end)//2
        self.tree_nodes[index] = self.est(start,mid,index*2)+self.est(mid+1,end,index*2+1)
        return self.tree_nodes[index]
        
    def interval_sum(self,start,end,index,left,right):
        if left>end or right<start:
            return 0
        if left<=start and right>=end:
            return self.tree_nodes[index]
        mid=(start+end)//2
        return self.interval_sum(start,mid,index*2,left,right)+self.interval_sum(mid+1,end,index*2+1,left,right)
    def update(self,start,end,index,target,value):
        if target<start or end<target:
            return
        self.tree_nodes[index]+=value
        if start==end:
            return
        mid = (start + end) // 2
        self.update(start,mid,index*2,target,value)
        self.update(mid+1,end,index*2+1,target,value)

for _ in range(N):
    seq.append(int(input()))
seg=segTree()
for _ in range(M+K):
    a,b,c=map(int,input().split()) # 1 수정 b번째 c로 변경 2 조회 b~c번째 수의 합.
    if a==1:
        seg.update(1,N,1,b,c)
    elif a==2:
        print(seg.interval_sum(1,N,1,b,c))
print(seg.tree_nodes)

