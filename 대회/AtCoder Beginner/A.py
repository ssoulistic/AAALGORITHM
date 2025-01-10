input=open("D:/python/AAALGORITHM/대회/test.txt",'r').readline
# import sys
# input=sys.stdin.readline
AB,AC,BC=input().split()
if AB=="<":
    if AC=="<":
        if BC=="<":
            print("B")
        else:
            print("C")
    else:
        if BC=="<":
            pass
        else:
            print("A")
else:
    if AC=="<":
        if BC=="<":
            print("A")
        else:
            pass
    else:
        if BC=="<":
            print("C")
        else:
            print("B")
    

    

    