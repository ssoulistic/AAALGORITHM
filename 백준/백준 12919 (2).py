input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
S = input().strip()
T = input().strip()

def check(word):
    if word==T:
        return 1
    elif len(word)==len(T) and word!=T:
        return 0
    
    if ((word+"A") in T or (word+"A")[::-1] in T) and check(word+"A"):
        return 1
    if ((word+"B")in T or (word+"B")[::-1] in T) and check((word+"B")[::-1]):
        return 1
    return 0 
print(check(S))
    