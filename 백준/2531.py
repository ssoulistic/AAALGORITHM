input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N,d,k,c=map(int,input().split())
sushi=[]
for _ in range(N):
    sushi.append(int(input()))
# 1. c가 포함되지 않은 연속된 k중 최대 +1
sushi=sushi*2
# 2. c가 포함된 연속된 k중 최대

event={}
for j in range(k):
    if event.get(sushi[j]):
        event[sushi[j]]+=1
    else:
        event[sushi[j]]=1
combo=len(event.keys())
answer=combo
i=0
while i+k<2*N:
    if event.get(sushi[i+k]):
        event[sushi[i+k]]+=1
    else:
        event[sushi[i+k]]=1
        combo+=1
    print(event)
    event[sushi[i]]-=1
    if event[sushi[i]]==0:
        del event[sushi[i]]
        combo-=1
    if c in event.keys():
        if answer<combo:
            answer=combo
    elif c not in event.keys():
        if answer<combo+1:
            answer=combo+1
    i+=1
    
print(answer)