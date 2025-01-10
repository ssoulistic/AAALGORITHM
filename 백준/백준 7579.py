input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N,M=map(int,input().split())
byte=list(map(int,input().split()))
costs=list(map(int,input().split()))
dp_cost_to_memory=[0 for _ in range(10001)]
pool=set([0])
for idc in range(N):
    temp=set()
    for p in pool:
        temp.add(costs[idc]+p)
    pool.update(temp)
    for p in sorted(pool,reverse=True):
        dp_cost_to_memory[p+costs[idc]]=max(dp_cost_to_memory[p+costs[idc]],dp_cost_to_memory[p]+byte[idc])
for idx,mem in enumerate(dp_cost_to_memory):
    if mem>=M:
        print(idx)
        break
        
    