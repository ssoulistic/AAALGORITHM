input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N,M=map(int,input().split())

class Node:
    def __init__(self):
        self.char=None
        self.isEnd=None
        self.children={}
class Trie:
    def __init__(self):
        self.root=Node()
        
    def insert(self,word):
        curr=self.root
        for char in word:
            if char not in curr.children:
                curr.children[char]=Node()
            curr=curr.children[char]
        curr.isEnd=True
    
    def startwith(self,word):
        curr=self.root
        for char in word:
            if char not in curr.children:
                return False
            curr=curr.children[char]
        return True
trie=Trie()
        
count=0

for _ in range(N):
    trie.insert(input().strip())

for _ in range(M):
    check=input().strip()
    if trie.startwith(check):
       count+=1
print(count) 