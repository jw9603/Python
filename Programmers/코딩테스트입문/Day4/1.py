def solution(n):
    return n // 7 + 1 if n %7 !=0 else n//7

if __name__ =='__main__':
    print(solution(7))
    print(solution(1))
    print(solution(15))