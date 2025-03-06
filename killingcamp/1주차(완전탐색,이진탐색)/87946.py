# 프로그래머스 - 피로도
# https://school.programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations
def solution(k, dungeons):
    # 최소 필요 피로도: 탐험하기 위해 가지고 있어야 하는 최소한의 피로도,
    # 소모 피로도: 던전을 탐험한 후 소모되는 피로도
    max_cnt = 0
    
    for perm in permutations(dungeons):
        current_k = k
        current_cnt = 0
        for min_required, cost in perm: # (최소 필요 피로도, 소모 피로도)
            if min_required <= current_k:
                current_k -= cost
                current_cnt += 1
            else:
                break
        max_cnt = max(max_cnt, current_cnt)
    return max_cnt
                
if __name__ == '__main__':
    k, dungeons = 80, [[80,20],[50,40],[30,10]]
    print(f"Result: {solution(k=k, dungeons=dungeons)}")