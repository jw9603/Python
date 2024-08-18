from collections import deque

def solution(priorities, location):
    
    queue = deque((i,p) for i,p in enumerate(priorities))  # i는 index, p는 우선순위
    answer = []
    
    while queue: 
        
        process = queue.popleft() # 1. 큐에서 대기중인 프로세스를 하나 꺼냄
        # print(process)
        if any(process[1] < q[1] for q in queue): # 2. 큐에서 대기중인 프로세스중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 process[1]를 다시 큐에 넣음.
            queue.append(process)
        else: # 3. 없다면 방금 꺼낸 프로세스를 실행
            answer.append(process)
            
    for i in answer:
        if i[0] == location:
            return answer.index(i) + 1
        
if __name__ == '__main__':
    print(solution([2, 1, 3, 2], 2))
    print(solution([1, 1, 9, 1, 1, 1], 0))    