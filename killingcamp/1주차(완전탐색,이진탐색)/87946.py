# 프로그래머스 - 피로도
# https://school.programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations
def solution(k, dungeons):
    max_dungeons = 0
    
    for perm in permutations(dungeons):
        current_k = k
        current_dungeons = 0
        
        for required_cost, cost in perm:
            if current_k >= required_cost:
                current_k -= cost
                current_dungeons += 1
            else:
                break
        max_dungeons = max(max_dungeons, current_dungeons)
    return max_dungeons
            
def solution(k, dungeons):
    max_dungeons = 0
    N = len(dungeons)
    used = [False] * N
    
    def dfs(cnt, energy):
        nonlocal max_dungeons
        max_dungeons = max(max_dungeons, cnt)
        
        if cnt == len(dungeons):
            return
        
        for i in range(N):
            if not used[i] and energy >= dungeons[i][0]:
                used[i] = True
                dfs(cnt + 1, energy - dungeons[i][1])
                used[i] = False
    dfs(0, k)
    
    return max_dungeons
                
if __name__ == '__main__':
    k, dungeons = 80, [[80,20],[50,40],[30,10]]
    print(f"Result: {solution(k=k, dungeons=dungeons)}")
