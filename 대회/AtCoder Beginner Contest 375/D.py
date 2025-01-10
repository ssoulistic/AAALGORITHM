input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
dic={}
S=input().strip()
answer=0

for i in range(len(S)):
    if dic.get(S[i]):
        for val in dic[S[i]]:
            if i-val>=2:
                answer+=i-val-1
        dic[S[i]].append(i)
    else:
        dic[S[i]]=[i]

print(answer)