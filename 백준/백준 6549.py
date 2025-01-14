input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline 

while True:
    n,*array=map(int,input().split())
    if n==0:
        break
    maximum=0
    for i in range(n):
        for height in range(1,array[i]+1):
            count=0
            for k in range(i,n):
                if array[k]>=height:
                    count+=1
                else:
                    break
            maximum=max(height*count,maximum)
    print(maximum)


            