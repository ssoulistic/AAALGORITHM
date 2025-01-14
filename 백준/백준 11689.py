input=open("sample.txt",'r').readline
# import sys
# input=sys.stdin.readline
from itertools import combinations
n=int(input())

def isPrime(number):
    for i in range(2,int((number)**(0.5))+1):
        if number % i ==0:
            return False
    return True


def get_dividers(number):
    results=set()
    for i in range(2,int((number)**(0.5))+1):
        if number % i ==0:
            if isPrime(i):
                results.add(i)
            if isPrime(number//i):
                results.add(number//i)
    return results

primes=get_dividers(n)
answer=0
for j in range(1,len(primes)+1):
    for k in combinations(primes,j):
        temp=1
        for l in k:
            temp*=l
        answer+=((-1)**(j+1))*(n//temp)
if primes:
    print(n-answer)
else:
    print(max(n-1,1))
