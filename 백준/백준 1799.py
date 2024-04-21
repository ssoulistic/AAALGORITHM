input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
chess=[]
for p in range(N):
    chess.append(list(map(int,input().split())))

left_cross=[False for _ in range(2*N-1)]

def bishop(right_coord,count):
    global answer
    if answer<count:
        answer=count
    if right_coord>2*N-1:
        return
    j=0
    Flag=True
    while j<=right_coord:
        nr,nc=j,right_coord-j
        if 0<=nr<N and 0<=nc<N:
            if chess[nr][nc]==1 and not left_cross[N-1+nc-nr]:
                Flag=False
                left_cross[N-1+nc-nr]=True
                bishop(right_coord+2,count+1)
                left_cross[N-1+nc-nr]=False
        j+=1
    if Flag:
        bishop(right_coord+2,count)
result=0
for i in range(2):
    answer=0
    bishop(i,0)  
    result+=answer
print(result)