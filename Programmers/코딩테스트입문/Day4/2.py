import math
def solution(n):
    return n*6 // math.gcd(n,6) / 6

if __name__ =='__main__':
    print(solution(6))
    print(solution(10))
    print(solution(4))