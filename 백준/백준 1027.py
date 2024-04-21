input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
building=list(map(int,input().split()))
look=[0 for _ in range(N)]

def check(build1_idx,build2_idx):
    incline=(building[build2_idx]-building[build1_idx])/(build2_idx-build1_idx)
    for k in range(build1_idx+1,build2_idx):
        incline2=(building[k]-building[build1_idx])/(k-build1_idx)
        if incline2>=incline:
            return False
    return True


for i in range(N):
    for j in range(i+1,N):
        if check(i,j):
            look[i]+=1
            look[j]+=1
    print(look)
print(max(look))
