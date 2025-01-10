input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
distance=0
start=[0,0]
for _ in range(N):
    end=list(map(int,input().split()))
    distance+=((start[0]-end[0])**2 + (start[1]-end[1])**2)**0.5
    start=end
end=[0,0]
distance+=((start[0]-end[0])**2 + (start[1]-end[1])**2)**0.5
print(distance)
    