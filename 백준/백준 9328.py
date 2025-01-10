input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
T=int(input())

for _ in range(T):
    graph=[]
    h,w=map(int,input().split())
    for _ in range(h):
        graph.append(list(input().strip()))
    keys=list(input().strip())
    
    print(keys)

# 문을 열수 있는지 확인
def match_key():
    return

# 진입점 확인 => bfs 탐색 => 문을 만나면 저장 => 열쇠 획득시 queue에 넣기
# 열쇠가 먼저 만나면 문을 딸 수 있고, 문을 먼저 만나면, 열쇠 획득시 queue에 추가해서 탐색 가능

