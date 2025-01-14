input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
def find(k):
    if group[k]!=k:
        group[k]=find(group[k])
    return group[k]
def union(a,b):
    a,b=find(a),find(b)
    if a!=b:
        group[max(a,b)]=min(a,b)
        return True
    return False

while True:
    m,n=map(int,input().split())
    if m==0 and n==0:
        break
    group=[i for i in range(m)]
    result=0
    street_lamps=[]
    total_cost=0
    for _ in range(n):
        x,y,z=map(int,input().split())
        street_lamps.append([z,x,y])
        total_cost+=z
    street_lamps.sort()
    for cost,house1,house2 in street_lamps:
        if union(house1,house2):
            result+=cost
    print(total_cost-result)