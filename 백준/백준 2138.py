input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
now=list(map(int,list(input().strip())))
target=list(map(int,list(input().strip())))

answer=[]
def click(idx,count,before):
    if idx==N-1:
        if now[idx]!=target[idx]:
            if before==[True,False] or before==[False,True]:
                answer.append(count)
        else:
            if before==[True,True] or before==[False,False]:
                answer.append(count)
        return

    if now[idx]!=target[idx]: # 다를 경우
        if before==[True,True] or before==[False,False]:
            click(idx+1,count+1,[before[-1],True])
        else:
            click(idx+1,count,[before[-1],False])
    else: # 같을경우 
        if before==[True,True] or before==[False,False]:
            click(idx+1,count,[before[-1],False])
        else:
            click(idx+1,count+1,[before[-1],True])

if now[0]!=target[0]: # 다를때 홀수번
    click(1,1,[True,False])
    click(1,1,[False,True])
else: # 같으면
    click(1,0,[False,False])
    click(1,2,[True,True])

if answer:
    print(min(answer))
else:
    print(-1)