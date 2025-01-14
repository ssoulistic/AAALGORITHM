input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline

# 켜진곳 기준 => 홀수번 영향
# 꺼진곳 => 짝수번 영향

bulb=[]
for _ in range(10):
    bulb.append(list(input().strip()))

# 0 번 인덱스 => 모두 안누른 경우 or 아래, 자신, 오른쪽 중 2개를 누른 경우
