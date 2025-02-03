input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline

# 부등호 수
k=int(input())
inequal=input().split()
minimum="10_000_000_000"
maximum="0"
def dfs(idx1,numbers):
    global minimum
    global maximum
    if idx1>=k+1:
        num="".join(map(str,numbers))
        if int(num)<int(minimum):
            minimum=num
        if int(num)>int(maximum):
            maximum=num
        return
    for i in range(10):
        if i not in numbers:
            if (inequal[idx1-1]=="<" and numbers[-1]<i) or (inequal[idx1-1]==">" and numbers[-1]>i):
                dfs(idx1+1,numbers+[i])
    return
for i in range(10):
    dfs(1,[i])
print(maximum)
print(minimum)