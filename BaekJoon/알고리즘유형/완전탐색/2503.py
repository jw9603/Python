# 백준 2503. 숫자 야구
# https://www.acmicpc.net/problem/2503
import sys
from itertools import permutations
N = int(sys.stdin.readline().strip())
questions = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
def count(num1, num2):
    strike, ball = 0, 0
    for i in range(3):
        if num1[i] == num2[i]:
            strike += 1
        elif num1[i] in num2:
            ball += 1
    return strike, ball


def sol(N, questions):
    candidates = list(permutations(range(1, 10), 3))
    cnt = 0
    
    for candidate in candidates:
        candidate_str = ''.join(map(str, candidate))
        valid = True
        
        for question, strike, ball in questions:
            question_str = str(question)
            s, b = count(candidate_str, question_str)
            
            if s != strike or b != ball:
                valid = False
                break
        if valid:
            cnt += 1
    return cnt
print(sol(N=N, questions=questions))
            