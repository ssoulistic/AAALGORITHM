input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
N,K=map(int,input().split())
S=input().strip()
one_block=0
answer_stack=[]
before_kth=[]
i=0
added=False
while i<N:
    if S[i]=="1":
        if i>=1 and S[i-1]!=S[i]:
            one_block+=1
        elif i==0:
            one_block=1
        answer_stack.append(S[i])
    elif S[i]=="0":
        if one_block==K-1:
            before_kth.append(S[i])
        elif one_block==K:
            answer_stack.extend(before_kth)
            added=True
        else:
            answer_stack.append(S[i])
    i+=1
if not added:
    answer_stack.extend(before_kth)
print("".join(answer_stack))