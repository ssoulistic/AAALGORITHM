input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())

class Node:
    def __init__(self):
        self.key=None
        self.data=None
        self.children={}

class Trie:
    def __init__(self):
        self.root=Node()
        
    def insert(self,String):
        curr=self.root
        for char in String:
            if char not in curr.children:
                curr.children[char]=Node()
            curr=curr.children[char]
            curr.key=char
        curr.data=String
    
    def findSub(self,String):
        curr=self.root
        for char in String:
            if char not in curr.children:
                curr=self.root
                if char in self.root.children:
                    curr=curr.children[char]
            else:
                curr=curr.children[char]
            if curr.data:
                return True
        return False
    
trie=Trie()
for _ in range(N):
    trie.insert(input().strip())
Q=int(input())
for _ in range(Q):
    if trie.findSub(input().strip()):
        print("YES")
    else:
        print("NO")
    
    