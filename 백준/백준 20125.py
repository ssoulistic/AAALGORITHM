input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline 
N=int(input())
graph=[]
for _ in range(N):
    graph.append(list(input().strip()))

head=[]
heart=[]
left_arm=0
right_arm=0
waist=0
left_leg=0
right_leg=0
for r in range(len(graph)):
    for c in range(len(graph[0])):
        if not head:
            if graph[r][c]=="*":
                head=[r,c]
                heart=[r+1,c]


ri=heart[0]
ci=heart[1]
# arm
while 0<=ri<len(graph) and 0<=ci<len(graph[0]):
    if graph[ri][ci]=="*":
        left_arm=heart[1]-ci
    ci-=1

ri=heart[0]
ci=heart[1]
while 0<=ri<len(graph) and 0<=ci<len(graph[0]):
    if graph[ri][ci]=="*":
        right_arm=ci-heart[1]
    ci+=1  

ri=heart[0]
ci=heart[1]
leg_start=-1
while 0<=ri<len(graph) and 0<=ci<len(graph[0]):
    if graph[ri][ci]=="*":
        waist=ri-heart[0]
        leg_start=ri
    ri+=1  

ri=leg_start
ci=heart[1]-1
while 0<=ri<len(graph) and 0<=ci<len(graph[0]):
    if graph[ri][ci]=="*":
        left_leg=ri-leg_start
    ri+=1

ri=leg_start
ci=heart[1]+1
while 0<=ri<len(graph) and 0<=ci<len(graph[0]):
    if graph[ri][ci]=="*":
        right_leg=ri-leg_start
    ri+=1
print(heart[0]+1,heart[1]+1)
print(left_arm,right_arm,waist,left_leg,right_leg)
            

