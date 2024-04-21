class Node(object):
    def __init__(self,key,data=None):
        self.key=key
        self.data=data
        self.children={}
class Trie(object):
    def __init__(self):
        self.head=Node(None)
    
    def insert(self,string):
        current_node=self.head
        for char in string:
            if char not in current_node.children:
                current_node.children[char]=Node(char)
            current_node=current_node.children[char]
        current_node.data=string
    
    def auto_input_count(self,current_node,count):
        if count==0:
            current_node=self.head
        # 1. 처음 입력 => 1
        if current_node.data!=None:
            result.append(count)
            if not current_node.children:
                return
            
        for child in current_node.children.values():
            if len(current_node.children)==1 and current_node.data==None:
                if count==0:
                    count+=1
                self.auto_input_count(child,count)
            else:
                self.auto_input_count(child,count+1)
        
        # 2. 그 이후 child 가 한개면 count 증가 없이 이어감
        # 2-1. 아닐경우 count+1
        # 3. 도중에 data가 존재하면 result에 count 값을 추가
            
input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline

while True:
    x=input().strip()
    if x=='':
        break
    if x.isdigit():
        trie=Trie()
        result=[]
        for _ in range(int(x)):
            trie.insert(input().strip())
        trie.auto_input_count(None,0)
        print(f'{sum(result)/len(result):.2f}')