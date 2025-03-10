# 프로그래머스 후보키
# https://school.programmers.co.kr/learn/courses/30/lessons/42890
# 풀이 1
def is_unique(comb, relation):
    global n
    result = {tuple(row[i] for i in comb) for row in relation}
    
    return len(result) == n
    
def is_minimal(comb, candidates):
    for key in candidates:
        if set(key) <= set(comb):  
            return False
    return True

def solution(relation):
    global n
    candidates = []
    n = len(relation)  # 행 개수
    m = len(relation[0])  # 열 개수

    def dfs(start, curr):
        if len(curr) == size:  
            if is_unique(curr, relation) and is_minimal(curr, candidates):  
                candidates.append(curr[:])  
            return  

        for i in range(start, m):
            curr.append(i)
            dfs(i + 1, curr)
            curr.pop() 
        
    for size in range(1, m + 1):  # 크기 1부터 m까지 모든 조합 고려
        dfs(0, [])
    
    return len(candidates)

from itertools import combinations
def is_unique(comb, relation):
    global n
    result = {tuple(row[i] for i in comb) for row in relation}
    return len(result) == n

def is_minimal(comb, candidates):
    for key in candidates:
        if set(key) <= set(comb):
            return False
    return True
# 풀이 2
def solution(relation):
    global n
    n = len(relation)
    m = len(relation[0])
    candidates = []
    
    for k in range(1, m + 1):
        for comb in combinations(range(m), k):
            if is_unique(comb, relation) and is_minimal(comb, candidates):
                candidates.append(comb)
    return len(candidates)