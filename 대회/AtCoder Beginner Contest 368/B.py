input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
integers=list(map(int,input().split()))
count=0
integers.sort(reverse=True)
while len(integers)>1:
    integers[0]-=1
    integers[1]-=1
    count+=1
    integers.sort(reverse=True)
    while integers and integers[-1]==0:
        integers.pop()
print(count)
    
    