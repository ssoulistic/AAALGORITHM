input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
sign=input().strip()
sm=[[0 for _ in range(N)] for _ in range(N)]
acc=[[0 for _ in range(N)] for _ in range(N)]
k=0
for i in range(N):
    for j in range(i,N):
        sm[i][j]=sign[k]
        k+=1
answer=[]
def dfs(idx):
    global answer
    if idx==N:
        if not answer:
            print(*acc,sep="\n")
            for i in range(idx):
                answer.append(acc[i][i])
        return
    for i in range(-10,11):
        for r in range(idx):
            if (sm[r][idx]=="+" and acc[r][idx-1]+i>0) or (sm[r][idx]=="-" and acc[r][idx-1]+i<0) or (sm[r][idx]=="0" and acc[r][idx-1]+i==0):
                acc[r][idx]=acc[r][idx-1]+i
                dfs(idx+1)
        for r in range(idx):
            acc[r][idx]=0
    return

for i in range(-10,11):
    acc[0][0]=i
    dfs(1)
    acc[0][0]=0
# print(*sm,sep="\n")
print("##")
print(answer)