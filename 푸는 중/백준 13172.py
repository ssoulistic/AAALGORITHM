input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
M=int(input())
mod=1000000007
def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a
# b의-1(mod) == b의 x-2승(mod)
def condiv(n,mul):
    result=1
    while mul>0:
        if mul % 2 ==1:
            result=(result*n) % mod
        n=(n*n) % mod
        mul//=2
    return result
        
answer=0
for _ in range(M):
    N,S=map(int,input().split())
    d=gcd(N,S)
    answer += (((S//d)*(condiv(N//d,mod-2) % mod))) % mod
print(answer %mod)