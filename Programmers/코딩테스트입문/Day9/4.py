def factorial(num):
    if num <=1:
        return 1
    return factorial(num-1) * num
def solution(balls, share):
    return factorial(balls) / (factorial(balls-share) * factorial(share))

############## 다른 풀이 ###############
import math

def solution(balls,share):
    return math.comb(balls,share)
############## 다른 풀이 ###############

if __name__ == '__main__':
    
    print(solution(3,2))
    print(solution(5,3))