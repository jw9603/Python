def solution(n):
    return sum([i for i in range(1,n+1) if i%2 == 0])

if __name__ =='__main__':
    print(solution(10))
    print(solution(4))