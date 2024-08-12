# https://school.programmers.co.kr/learn/courses/30/lessons/181833
# 특별한 이차원 배열 1



import numpy as np
def solution(n):
    return(np.eye(n,dtype=np.int8).tolist())

########### 다른 풀이 ####################
def solution(n):
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        ans[i][i] = 1
    return ans
########### 다른 풀이 ####################

if __name__ == '__main__':
    print(solution(3))
    print(solution(6))
    print(solution(1))