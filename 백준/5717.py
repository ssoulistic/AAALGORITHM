input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
while True:
    M,F=map(int,input().split())
    if M==0 and F==0:
        break
    print(M+F)