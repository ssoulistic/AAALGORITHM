input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=input().strip()
answer=[0 for _ in range(10)]
acc=0
digit=0
answer[0]=-1
while digit<len(N):
    left,now,right=N[:digit],N[digit],N[digit+1:]
    if left:
        acc+=int(left)*10**(len(N)-1-digit)
        answer[0]-=10**(len(N)-digit)
    
    for i in range(int(now)):
        answer[i]+=10**(len(N)-1-digit)
    if right:
        answer[int(now)]+=int(right)+1
    else:
        answer[int(now)]+=1
    digit+=1
for a in range(10):
    answer[a]+=acc
print(*answer)
    

