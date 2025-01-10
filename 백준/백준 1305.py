input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
L=int(input())
T=input().strip()
def F(word):
    l=len(word)
    table=[0 for _ in range(l)]
    
    prefix_idx=0
    for idx in range(1,l):
        while prefix_idx>0 and word[prefix_idx]!=word[idx]:
            prefix_idx=table[prefix_idx-1]
        if word[prefix_idx]==word[idx]:
            prefix_idx+=1
            table[idx]=prefix_idx
        
    return prefix_idx


print(L-F(T))