input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
X,Y,D,T=map(float,input().split())
dist=(X**2+Y**2)**0.5
q=dist//D
# 점프가 더 느린경우
if D<T:
    print(dist)
# 점프가 짧은 경우
elif dist>2*D:
    print(min((q+1 if dist%D else 0)*T,dist-q*D+q*T,abs(dist-(q+1)*D)+(q+1)*T))
# 점프가 긴 경우
elif dist<=2*D:
    print(min(2*T,dist-q*D+q*T,abs(dist-(q+1)*D)+(q+1)*T))
    

        