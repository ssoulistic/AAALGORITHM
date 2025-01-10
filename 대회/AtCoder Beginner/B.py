input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
N,M=map(int,input().split())
Taro=[False for _ in range(N)]
for _ in range(M):
    family,gender=input().split()
    family=int(family)
    if Taro[family-1]:
        print("No")
    else:
        if gender=="M":
            Taro[family-1]=True
            print("Yes")
        else:
            print("No")
        
