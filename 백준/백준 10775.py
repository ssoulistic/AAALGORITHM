input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline

G=int(input())
P=int(input())
gates=[False for _ in range(G)]

for k in range(P):
    gi=int(input())
    dock=False
    for i in range(gi-1,-1,-1):
        if not gates[i]:
            gates[i]=True
            dock=True
            break
    if not dock:
        break
print(k)
    
        
    