input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
bingo=[]
for i in range(3):
    bingo.append([0+3*i,1+3*i,2+3*i])
    bingo.append([0+i,3+i,6+i])
bingo.append([0,4,8])
bingo.append([2,4,6])
print(bingo)


while True:
    query=input().strip()
    if query=="end":
        break
    # 첫번쨰 사람이 x 두번째가 O
    # 1. x가 우승 => x개수가 O보다 1개 많음
    # 2. O가 우승 => x개수==O개수
    # 3. 칸이 꽉참 => x5개 o 4개
    Xs=query.count("X")
    Os=query.count("O")
    winner=[]
    answer="invalid"
    for a,b,c in bingo:
        if query[a]==query[b]==query[c]!=".":
            winner.append(query[a])
    if len(set(winner))==1:
        if winner[0]=="X":
            if Xs==Os+1:
                answer="valid"
        elif winner[0]=="O":
            if Xs==Os:
                answer="valid"
    elif len(set(winner))==0:
        if Xs==5 and Os==4:
            answer="valid"
    print(answer)
    # bingo x , bingo o , bingo none 중 1
    
    