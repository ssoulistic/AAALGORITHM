input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
from collections import deque
S=input().strip()
T=input().strip()

# 1. 문자열 뒤에 A를 추가
# 2. 문자열 뒤에 B를 추가하고 문자열 뒤집기
answer=0
queue=deque()
if S in T or S[::-1] in T:
    queue.append(S)
while queue:
    print(queue)
    word=queue.popleft()
    if word==T:
        answer=1
    case1=word+"A"
    case2=(word+"B")[::-1]
    if case1 in T or case1[::-1] in T:
        queue.append(case1)
    if case2 in T or case2[::-1] in T:
        queue.append(case2)
print(answer)