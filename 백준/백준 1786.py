input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
T=input()
P=input()
def failurefunciton(pattern):
    table=[0 for _ in range(len(pattern))]
    
    prefix_idx=0
    for idx in range(1,len(pattern)):
        while prefix_idx>0 and pattern[prefix_idx]!=pattern[idx]:
            prefix_idx=table[prefix_idx-1]
        if pattern[prefix_idx]==pattern[idx]:
            prefix_idx+=1
            table[idx]=prefix_idx
    return table

def kmp(target,pattern):
    table=failurefunciton(pattern)
    results=[]
    pattern_idx=0
    for idx in range(len(target)):
        while pattern_idx>0 and pattern[pattern_idx]!=target[idx]:
            pattern_idx=table[pattern_idx-1]
        if pattern[pattern_idx]==target[idx]:
            if pattern_idx==len(pattern)-1:
                results.append(idx-len(pattern)+2)
                pattern_idx=table[pattern_idx]
            else:
                pattern_idx+=1
    return results

result=kmp(T,P)
print(len(result))
print(*result)