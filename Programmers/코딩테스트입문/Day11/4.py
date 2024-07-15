def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)
def solution(n):
    for i in range(1,12):
        if n < factorial(i):
            return i-1
        
if __name__ == '__main__':
    print(solution(3628800))
    print(solution(7))