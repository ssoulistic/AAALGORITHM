input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=input().strip()
digit=len(N)
N=int(N)
answer=0
while digit>0:
    answer+=(N-10**(digit-1)+1)*digit
    N=10**(digit-1)-1
    digit-=1
print(answer)