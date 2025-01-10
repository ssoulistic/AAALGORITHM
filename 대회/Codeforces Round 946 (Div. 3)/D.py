input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    instruction=input().strip()
    coord_R=[0,0]
    coord_H=[0,0]
    answer=[]
    for command in instruction:
        if command in ["N","S"]:
            if coord_R[1]==coord_H[1]:
                if "R" in answer:
                    if command=="N":
                        coord_H[1]+=1
                    elif command=="S":
                        coord_H[1]-=1
                    answer.append("H")
                else:
                    if command=="N":
                        coord_R[1]+=1
                    elif command=="S":
                        coord_R[1]-=1
                    answer.append("R")
            elif coord_R[1]>coord_H[1]:
                if command=="N":
                    coord_H[1]+=1
                    answer.append("H")
                elif command=="S":
                    coord_R[1]-=1
                    answer.append("R")
            elif coord_R[1]<coord_H[1]:
                if command=="N":
                    coord_R[1]+=1
                    answer.append("R")
                elif command=="S":
                    coord_H[1]-=1
                    answer.append("H")
        elif command in ["E","W"]:
            if coord_R[0]==coord_H[0]:
                if "R" in answer:
                    if command=="E":
                        coord_H[0]+=1
                    elif command=="W":
                        coord_H[0]-=1
                    answer.append("H")
                else:
                    if command=="E":
                        coord_R[0]+=1
                    elif command=="W":
                        coord_R[0]-=1
                    answer.append("R")
            elif coord_R[0]>coord_H[0]:
                if command=="E":
                    coord_H[0]+=1
                    answer.append("H")
                elif command=="W":
                    coord_R[0]-=1
                    answer.append("R")
            elif coord_R[0]<coord_H[0]:
                if command=="E":
                    coord_R[0]+=1
                    answer.append("R")
                elif command=="W":
                    coord_H[0]-=1
                    answer.append("H")
    if coord_H==coord_R and len(set(answer))==2:
        print("".join(answer))
    else:
        print("NO")