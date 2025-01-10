input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
w=int(input())

class Node(object):
    def __init__(self,key=None):
        self.key=None
        self.word=None
        self.children={}
    
class Trie(object):
    def __init__(self):
        self.root=Node()
    
    def insert(self,string):
        curr=self.root
        for char in string:
            if char not in curr.children:
                curr.children[char]=Node(char)
            curr=curr.children[char]
        curr.word=string
        
    def search(self,string):
        curr=self.root
        for char in string:
            if char not in curr.children:
                return False
            curr=curr.children[char]
        if curr.word:
            return True
        return False

trie=Trie()
# trie 등록
for _ in range(w):
    bog=input().strip()
    trie.insert(bog)

# 환산용 점수
score={1:0,2:0,3:1,4:1,5:2,6:3,7:5,8:11}

def dfs(board,coord,char_list,visited):
    global count
    global scoring
    global longest
    global check
    key="".join(char_list)
    if len(key)>8:
        return
    if trie.search(key):
        if not check.get(key):
            check[key]=True
            count+=1
            scoring+=score[len(key)]
            if len(longest)<len(key):
                longest=key
            elif len(longest)==len(key):
                longest=min(longest,key)
    r,c=coord
    for dr,dc in [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]:
        nr=r+dr
        nc=c+dc
        if 0<=nr<4 and 0<=nc<4 and not visited[nr][nc]:
            visited[nr][nc]=True
            char_list.append(board[nr][nc])
            dfs(board,[nr,nc],char_list,visited)
            char_list.pop()
            visited[nr][nc]=False
    return

input().strip()
# Boggle
b=int(input())
for _ in range(b):
    boggle=[]
    check={}
    scoring=0
    longest=""
    count=0
    for _ in range(4):
        boggle.append(list(input().strip()))
    input().strip()
    
    for rr in range(4):
        for cc in range(4):
            v=[[False for _ in range(4)] for _ in range(4)]
            v[rr][cc]=True
            dfs(boggle,[rr,cc],[boggle[rr][cc]],v)
    print(scoring,longest,count)