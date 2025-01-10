from collections import deque
def solution(N, number):
    limit=32000*N+1
    dp=[1e5 for _ in range(limit)]
    start=N
    queue=deque()
    count=1
    while start<limit:
        dp[start]=count
        queue.append(start)
        start=10*start+N    
        count+=1
    while queue:
        now=queue.popleft()
        for eq in [lambda x: x+N,lambda x: x-N, lambda x: x*N, lambda x: x//N]:
            next_num=eq(now)
            if 0<next_num<limit:
                if dp[next_num]>dp[now]+1:
                    dp[next_num]=dp[now]+1
                    queue.append(next_num)
    print(dp)
    print(dp[number])
    if dp[number]>8:
        return -1
    else:
        return dp[number]
solution(1,123)