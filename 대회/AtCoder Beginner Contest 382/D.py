input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
# sys.setrecursionlimit(10**9)
N,M=map(int,input().split())
answer=[]
def bt(seq):
    sz=len(seq)
    if sz==N:
        answer.append(seq)
        return
    for i in range(1 if sz==0 else seq[-1]+10, M-10*(N-sz-1)+1):
        nxt=seq[:]
        nxt.append(i)
        bt(nxt)
bt([])
print(len(answer))
for ans in answer:
    print(*ans)