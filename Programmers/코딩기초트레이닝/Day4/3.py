def solution(n):    
    return sum([i**2 for i in range(2,n+1,2)]) if n%2 == 0 else sum([i for i in range(1,n+1,2)])

if __name__ =='__main__':
    print(solution(7))
    print(solution(10))