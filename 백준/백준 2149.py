input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline

key=input().strip()
secret=input().strip()

mem=[]
for p in range(len(key)):
    mem.append([key[p],p])
mem.sort()
dic={}
for m in range(len(mem)):
    dic[mem[m][1]]=m


n=len(secret)//len(key)
graph=[["" for _ in range(len(key))] for _ in range(n)]

for c in range(len(key)):
    for r in range(n):
        graph[r][c]=secret[n*c+r]

for r in range(n):
    for c in range(len(key)):
        print(graph[r][dic[c]],end="")
    
