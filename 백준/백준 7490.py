input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline

def find_exp(depth):
    if depth==num-1:
        # 결과가 0이면 print, return
        value=eval("".join("".join(exp).split()))
        if value==0:
            print("".join(exp))
        return
    sign=[" ","+","-"]
    for s in sign:
        exp[2*depth+1]=s
        find_exp(depth+1)
        exp[2*depth+1]=" "
    return

N=int(input())
for _ in range(N):
    num=int(input())
    exp=list(" ".join([str(i+1) for i in range(num)]))
    find_exp(0)
    print()
    