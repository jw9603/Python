import math
def solution(n):
    for i in range(2,11):
        if math.factorial(i) == n:
            return i
        elif math.factorial(i) > n:
            return i-1

if __name__ =='__main__':
    print(solution(10))