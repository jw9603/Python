# 프로세스
# https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque
def solution(priorities, location):
    
    queue = deque((i,p) for i,p in enumerate(priorities))
    ans = []
    
    while queue:
        process = queue.popleft()
        
        if any(process[1] < q[1] for q in queue):
            queue.append(process)
        else:
            ans.append(process)
        
    
    return next((idx+1 for idx,i in enumerate(ans) if i[0] == location),None)

if __name__ == '__main__':
    print(solution([2, 1, 3, 2],2))
    print(solution([1, 1, 9, 1, 1, 1],0))