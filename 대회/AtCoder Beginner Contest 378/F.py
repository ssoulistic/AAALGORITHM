input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
degree=[0 for _ in range(N)]
for _ in range(N-1):
    u,v=map(int,input().split())
    degree[u-1]+=1
    degree[v-1]+=1
print(degree)
able=degree.count(2)
print(able)
print(able*(able-1)/2)

## 중간의 모든 degree가 3이여야 함