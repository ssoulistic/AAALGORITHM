input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N,M=map(int,input().split())
jewel=[]
for _ in range(M):
    jewel.append(int(input()))

def share(number):
    count=0
    for j in jewel:
        if j % number:
            count+=1
        count+=j//number
    return count

start=1
end=10**9

while start<end:
    mid=(start+end)//2
    if share(mid)>N:
        start=mid+1
    else:
        end=mid
print(end)
