def solution(n):
    return sum([i for i in range(n+1) if i%2==0])

if __name__=='__main__':
    print(solution(14))