input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline 
N=int(input())
up,down=N//2+N%2,N//2
for _ in range(N):
    print(up*"* ")
    print(down*" *")
