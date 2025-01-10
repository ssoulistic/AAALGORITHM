input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline


T=int(input())
for _ in range(T):
    x,y=map(int,input().split())
    distance=y-x
    max_speed=int(distance**0.5)
    if distance==0:
        print(0)
    elif max_speed**2+max_speed<distance:
        print(max_speed*2+1)
    elif max_speed**2<distance:
        print(max_speed*2)
    elif max_speed**2==distance:
        print(max_speed*2-1)
    