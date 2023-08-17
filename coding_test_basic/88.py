import math
def solution(a, b):
    answer = 0
    b //= math.gcd(a,b)
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
        
    return 1 if b==1 else 2

if __name__ =='__main__':
    print(solution(7,10))