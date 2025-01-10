input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
from bisect import *
# import sys
# input=sys.stdin.readline
H,W,Q=map(int,input().split())
answer=H*W
walls=[[i for i in range(W)] for _ in range(H)]
for _ in range(Q):
    R,C=map(int,input().split())
    r=R-1
    c=C-1
    if bisect_left(walls[r],c)==c:
        print(c,walls[r],bisect_left(walls[r],c))
        walls[r].remove(c)
    else:
        a=bisect_left(walls[r],c)
        b=bisect_right(walls[r],c)
        if 0<=a<W:
            walls[r].remove(a)
            answer-=1
        if 0<=b<W:
            walls[r].remove(b)
            answer-=1
        up,down=r,r
        while 0<=up<H:
            if bisect_left(walls[up],c)==c:
                walls[up].remove(c)
                answer-=1
                break
            else:
                up-=1
        while 0<=down<H:
            if bisect_left(walls[down],c)==c:
                walls[down].remove(c)
                answer-=1
                break
            else:
                down+=1
    
    
print(answer)