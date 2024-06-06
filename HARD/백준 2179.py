input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
words=[]
for _ in range(N):
    words.append(input().strip())

answer=[0,[]]
for i in range(N):
    if len(words[i])<=answer[0]:
        continue
    for j in range(i+1,N):
        if len(words[j])<=answer[0] or words[i]==words[j]:
            continue
        count=0
        for k in range(min(len(words[i]),len(words[j]))):
            if words[i][k]==words[j][k]:
                count+=1
            else:
                break
        if answer[0]<count:
            answer[0]=count
            answer[1]=[words[i],words[j]]
print(*answer[1],sep="\n")