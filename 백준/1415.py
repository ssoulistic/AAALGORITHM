input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
total=0
candies={}
for _ in range(N):
    K=int(input())
    total+=K
    if candies.get(K):
        candies[K]+=1
    else:
        candies[K]=1
print(total)
dp=[[0 for _ in range(total+1)] for _ in range(2)]
dp[0][0]=1
p=0
for k,v in candies.items():
    for j in range(v,0,-1):
        for i in range(total,k*j-1,-1):
            dp[(p+1)%2][i]+=dp[p%2][i-k*j]
        dp[(p+1)%2][k*j]+=1
    p+=1
print(dp[(p%2)])
            
    
def isPrime(num):
    if num==0 or num==1:
        return False
    for i in range(2,int((num)**0.5)+1):
        if num%i==0:
            return False
    return True

for i in range(2,total+1):
    if dp[i] and isPrime(i):
        j=2
        while i*j<=total:
            dp[i*j]=0
            j+=1
print(dp)
print(list(i for i in range(len(dp))))
print(sum(dp[2:]))
            
    