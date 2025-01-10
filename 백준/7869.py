input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
from math import *
x1,y1,r1,x2,y2,r2=map(float,input().split())
d=((x1-x2)**2+(y1-y2)**2)**0.5
R=max(r1,r2)
r=min(r1,r2)
if d<=R-r: #작은원이 큰 원 내부
    print(f'{round(r**2*pi,3):.3f}')
elif d>=R+r: # 겹치지 않음
    print(f'{0.000:.3f}')
else: 
    part1 = r1**2 * acos((d**2 + r1**2 - r2**2) / (2 * d * r1))
    part2 = r2**2 * acos((d**2 + r2**2 - r1**2) / (2 * d * r2))
    part3 = 0.5 * sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2))
    print(f'{round(part1+part2-part3,3):.3f}')
    
