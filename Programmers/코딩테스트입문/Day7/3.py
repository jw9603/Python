def solution(n, k):
    return n * 12000 + k * 2000 - (n // 10) * 2000

if __name__ =='__main__':
    print(solution(10,3))
    print(solution(64,6))