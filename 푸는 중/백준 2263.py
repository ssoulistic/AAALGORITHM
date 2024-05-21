input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
n=int(input())
inorder=list(map(int,input().split()))
postorder=list(map(int,input().split()))
# 중위 => left root right
# 후위 => left right root
coord={}
for i in range(n):
    coord[inorder[i]]=i

# 전위 => root left right
def guess_preorder(ist,iend,pst,pend):
    if ist>iend or pst>pend:
        return
    root=postorder[pend]
    print(root,end=" ")
    left=coord[root]-ist
    right=iend-coord[root]
    # 좌
    guess_preorder(ist,coord[root]-1,pst,pend-1-right)
    # 우
    guess_preorder(coord[root]+1,iend,pst+left,pend-1)
    

guess_preorder(0,n-1,0,n-1)
