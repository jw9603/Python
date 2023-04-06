import math

def solution(balls,share):
    return math.comb(balls,share)

if __name__ =='__main__':
    print(solution(30,16))