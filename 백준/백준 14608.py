input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline

K=int(input())
c=list(map(int,input().split()))
a,b,N=map(int,input().split())
dx=(b-a)/N
left_side=0
right_side=0
for k in range(N):
    x = a + k * dx  # 구간의 시작점
    f_x = sum(c[i] * (x ** (K - i)) for i in range(K + 1))
    right_side += f_x * dx  # f(x) * dx를 더해줌
for i in range(K+1):
    left_side+=(c[i]/(K-i+1)*(b**(K-i))-c[i]/(K-i+1)*(a**(K-i)))
epsilon=(left_side-right_side)/(b-a)
if 0<=epsilon<=dx:
    print(f'{epsilon:.4f}')
else:
    print(-1)