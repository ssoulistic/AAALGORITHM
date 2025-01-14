input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline

#! 분할하여 풀이
# for _ in range(3):
#     N=int(input())
#     coins=[]
#     for _ in range(N):
#         value,amount=map(int,input().split())
#         i=1
#         while amount>0:
#             ix=min(i,amount)
#             coins.append(value*ix)
#             i*=2
#             amount-=ix
#     total=sum(coins)
#     M=len(coins)
#     dp=[0 for _ in range(total//2+1)]
#     dp[0]=1
#     if total % 2==0 and max(coins)<=total//2:
#         for i in range(M):
#             for j in range(total//2,coins[i]-1,-1):
#                 if dp[j-coins[i]]:
#                     dp[j]=1    
#     print(dp[-1])

#! 탐색하여 풀이
def main():
    for _ in range(3):
        N=int(input())
        coins=[]
        total=0
        for _ in range(N):
            value,amount=map(int,input().split())
            total+=value*amount
            coins.append([value,amount])
        dp=[0 for _ in range(total//2+1)]
        dp[0]=1
        if total % 2==0:
            for i in range(N):
                if dp[-1]:
                    break
                v,a=coins[i]
                for j in range(total//2,v-1,-1):
                    if dp[j-v]:
                        for k in range(a):
                            if j+v*k<=total//2:
                                dp[j+v*k]=1
                            else:
                                break
        print(dp[-1])
main()