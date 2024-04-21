input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
given=input().strip()
a=given.count("a")
b=given.count("b")
N=len(given)
sample="a"*a+"b"*b
answer=N

def check(a,b):
    i=0
    count=0
    while i<N:
        if a[i]!=b[i]:
            count+=1
        i+=1
    return count//2

for j in range(a+1):
    sample="a"*(a-j)+"b"*b+"a"*j
    result=check(given,sample)
    if answer>result:
        answer=result
    
for k in range(b+1):
    sample="b"*(b-k)+"a"*a+"b"*k
    result=check(given,sample)
    if answer>result:
        answer=result
print(answer)