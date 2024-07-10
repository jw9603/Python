def solution(n):
    return len([i for i in range(1,n+1) if n%i==0])

if __name__ == '__main__':
    print(solution(20))
    print(solution(100))