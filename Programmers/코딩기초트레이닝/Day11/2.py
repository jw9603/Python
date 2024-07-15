def solution(n, k):
    return [i for i in range(1,n+1) if i % k == 0]

if __name__ == '__main__':
    print(solution(10,3))
    print(solution(15,5))