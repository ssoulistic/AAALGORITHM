# 옮기는거 상대적 => 최대 25만 정도 될것 같고, 왼빨오파, 왼파오빨 => 벽붙은 경우 빼면 똑같은듯..?
# 테케) 벽의 색깔에 따라 달라질수도.
# 최종 R B => 왼쪽으로 R모으기 오른쪽으로 B모으기
# B R => 오른쪽으로 R모으기, 왼쪽으로  B모으기.


input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
N=int(input())
balls=input().strip()
left_end=balls[0]
right_end=balls[-1]

i=0
red=[]
blue=[]
R,B=0,0
while i<N:
    if balls[i]=="R":
        R+=1
        if B:
            blue.append(B)
            B=0
    elif balls[i]=="B":
        B+=1
        if R:
            red.append(R)
            R=0
    i+=1
if R:
    red.append(R)
if B:
    blue.append(B)
print(red,blue)
# RB
answer=N
if left_end=="R":
    answer=min(answer,sum(red[1:]))
else:
    answer=min(answer,sum(red))
if right_end=="B":
    answer=min(answer,sum(blue[:-1]))
else:
    answer=min(answer,sum(blue))

# BR
if left_end=="B":
    answer=min(answer,sum(blue[1:]))
else:
    answer=min(answer,sum(blue))
if right_end=="R":
    answer=min(answer,sum(red[:-1]))
else:
    answer=min(answer,sum(red))

print(answer)
    