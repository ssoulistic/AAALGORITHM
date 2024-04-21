class Node(object):
    def __init__(self,key):
        self.key=key
        self.children={}
        
class Trie(object):
    def __init__(self):
        self.head=Node(None)
    
    def insert(self,words):
        current_node=self.head
        for word in words:
            if word not in current_node.children:
                current_node.children[word]=Node(word)
            current_node=current_node.children[word]
    
    def printall(self,current_node,depth):
        if depth==0:
            current_node=self.head
        for child in sorted(current_node.children):
            print("--"*depth+child)
            if current_node.children:
                self.printall(current_node.children[child],depth+1)
        
       


input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
trie = Trie()
for _ in range(N):
    k,*floor=input().split()
    trie.insert(floor)
trie.printall(None,0)
    
    
    
    