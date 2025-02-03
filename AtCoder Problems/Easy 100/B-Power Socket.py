input=open("sample.txt","r").readline
# import sys
# input=sys.stdin.readline
A,B=map(int,input().split())
answer=0
if A>=B>1:
    answer = 1
else:
    p,q=divmod(B-A,A-1)
    answer= 1 + p + (1 if q else 0)
print(answer)