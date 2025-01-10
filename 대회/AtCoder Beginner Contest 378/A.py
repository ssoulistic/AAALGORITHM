input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
a,b,c,d=map(int,input().split())
dict={}
count=0
for i in [a,b,c,d]:
    if dict.get(i):
        dict[i]+=1
    else:
        dict[i]=1

for v in dict.values():
    count+=v//2
print(count)
        
        