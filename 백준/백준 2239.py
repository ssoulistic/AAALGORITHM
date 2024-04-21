input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
sudoku=[]
# 각 숫자에 대해(row=숫자) 각 행에 그 숫자가 존재하는지 체크.
row_check=[[False for _ in range(9)] for _ in range(9)]
# 각 숫자에 대해(row=숫자) 각 열에 그 숫자가 존재하는지 체크.
col_check=[[False for _ in range(9)] for _ in range(9)]
# 각 숫자에 대해(row=숫자) 차례로 블럭에 그 숫자가 존재하는지 체크
square_check=[[False for _ in range(9)] for _ in range(9)]
for _ in range(9):
    sudoku.append(list(map(int,list(input().strip()))))
blank=[]

for r in range(9):
    for c in range(9):
        if sudoku[r][c]!=0:
            row_check[sudoku[r][c]-1][r]=True
            col_check[sudoku[r][c]-1][c]=True
            square_check[sudoku[r][c]-1][3*(r//3)+c//3]=True
        else:
            blank.append([r,c])
# 1.놓을 수 있는지 확인 => 가로,세로,네모
def solve(idx):
    if idx==len(blank):
        for ss in sudoku:
            print(''.join(map(str,ss)))
        return True
    r,c=blank[idx]
    for i in range(1,10):
        if row_check[i-1][r]==False and col_check[i-1][c]==False and square_check[i-1][3*(r//3)+c//3]==False:
            row_check[i-1][r]=True
            col_check[i-1][c]=True
            square_check[i-1][3*(r//3)+c//3]=True
            sudoku[r][c]=i
            if solve(idx+1):
                return True
            sudoku[r][c]=0
            row_check[i-1][r]=False
            col_check[i-1][c]=False
            square_check[i-1][3*(r//3)+c//3]=False
    return False
solve(0)