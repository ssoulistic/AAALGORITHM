input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
S=input().strip()
count=0
i=0
while i<N-2:
    if S[i:i+3]=="#.#":
        count+=1
        i+=2
    else:
        i+=1
print(count)