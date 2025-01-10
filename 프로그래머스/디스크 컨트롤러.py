from heapq import *
def solution(jobs):
    n=len(jobs)
    heapify(jobs)
    answer = 0
    now=0
    queue=[]
    while jobs or queue:
        if jobs and jobs[0][0]>=now:
            now=jobs[0][0]
        while jobs and jobs[0][0]<=now:
            start,time=heappop(jobs)
            heappush(queue,[time,start])
        time,start=heappop(queue)
        now+=time
        answer+=now-start
    return answer//n

jobs = [[1, 4], [7, 9], [1000, 3]]
print(solution(jobs))
# return = 5

jobs = [[7, 8], [3, 5], [9, 6]]
print(solution(jobs))
# return = 9

jobs = [[0, 3], [10, 1]]
print(solution(jobs))
# return 2

jobs = [[0, 3], [4, 4], [5, 3], [7, 1]]
print(solution(jobs))
# return 4