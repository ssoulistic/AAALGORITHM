input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
for _ in range(N):
    K=int(input())
    answer="GoHanGang"
    while K>1:
        if K%2:
            answer="Gazua"
            break
        K//=2
    print(answer)
            