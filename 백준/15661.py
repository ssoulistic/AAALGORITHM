input=open("sample.txt","r").readline
# import sys
# input=sys.stdin.readline
N=int(input())
abil=[]
total=0
for _ in range(N):
    abil.append(list(map(int,input().split())))
for idx in range(N):
    total+=sum(abil[idx])
diff=1e9
team=[1 for _ in range(N)]
def selection(SA,SB,picked,idx):
    global diff
    if picked>0 and picked<=N//2:
        diff=min(diff,abs(SA-SB))
    elif picked>N//2:
        return
    if idx>=N or SA>SB:
        return
    PA,PB=0,0
    
    team[idx]=0
    for j in range(N):
        if team[j]==1:
            PB+=abil[idx][j]+abil[j][idx]
        else:
            PA+=abil[idx][j]+abil[j][idx]
    selection(SA+PA,SB-PB,picked+1,idx+1)
    team[idx]=1

    selection(SA,SB,picked,idx+1)
    return
selection(0,total,0,0)
print(diff)