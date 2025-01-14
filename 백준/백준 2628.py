input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
w,h=map(int,input().split())
n=int(input())
rectangle=[[0],[0]]
for _ in range(n):
    direction,line=map(int,input().split())
    rectangle[direction].append(line)
rectangle[0].append(h)
rectangle[1].append(w)
rectangle[0].sort()
rectangle[1].sort()
area=0
for i in range(len(rectangle[0])-1):
    for j in range(len(rectangle[1])-1):
        area=max(area,(rectangle[0][i+1]-rectangle[0][i])*(rectangle[1][j+1]-rectangle[1][j]))
print(area)