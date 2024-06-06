# python 3.6이상 부터는 dictionary.items() 사용시 저장된 순서가 보장됨.
    
input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
prefix={}
words=[]
for idx in range(N):
    word=input().strip()
    words.append(word)
    for i in range(1,len(word)+1):
        char=word[:i]
        if prefix.get(char):
            prefix[char].append(idx)
        else:
            prefix[char]=[idx]
longest=[0,[]]
for k,v in prefix.items():
    if len(k)>longest[0]:
        if len(v)>1:
            longest[0]=len(k)
            longest[1]=[v[0],v[1]]
print(words[longest[1][0]],words[longest[1][1]],sep="\n")