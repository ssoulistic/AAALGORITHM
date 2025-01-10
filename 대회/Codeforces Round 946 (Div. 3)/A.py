input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
t=int(input())
for _ in range(t):
    screen=[]
    x,y=map(int,input().split())
    for _ in range(y//2):
        screen.append(7)
    if y % 2:
        screen.append(11)
    
    if screen:
        i=0
        while x>0 and i<len(screen):
            x-=screen[i]
            i+=1
    if x>0:
        for _ in range(x//15):
            screen.append(0)
        if x % 15:
            screen.append(x%15)
    print(len(screen))
            
            
            
        
    
        
    