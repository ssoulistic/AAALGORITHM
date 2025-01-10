input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    b=input().strip()
    s=list(set(b))
    dic={}
    s.sort()
    for i in range(len(s)):
        dic[s[i]]=s[len(s)-1-i]
    for j in range(n):
        print(dic[b[j]],end="")
    print()