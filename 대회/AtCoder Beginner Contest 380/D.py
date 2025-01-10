input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
S=input().strip()
N=len(S)
Q=int(input())
K=list(map(int,input().split()))
alphabet_convert={}

for i in range(26):
    alphabet_convert[chr(ord('a')+i)]=chr(ord('A')+i)
    alphabet_convert[chr(ord('A')+i)]=chr(ord('a')+i)

def mirrored(x):
    mirrored=0
    while x>0:
        if x%2==1:
            mirrored+=1
            mirrored%=2
        x/=2
    return mirrored
for k in K:
    p,q=divmod(k-1,N)
    if mirrored(p):
        print(alphabet_convert[S[q]],end=" ")
    else:
        print(S[q],end=" ")
    