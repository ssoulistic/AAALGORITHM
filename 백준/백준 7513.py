input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
T=int(input())
for i in range(T):
    m=int(input())
    word=[]
    for _ in range(m):
        word.append(input().strip())
    n=int(input())
    print(f'Scenario #{i+1}:')
    
    for _ in range(n):
        temp=""
        k,*idxs=map(int,input().split())
        for j in range(k):
            temp+=word[idxs[j]]
        print(temp)
    print()