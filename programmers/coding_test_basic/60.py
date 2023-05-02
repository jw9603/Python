def solution(n):
 
    return sorted(i for i in range(1,n+1) if n % i == 0)

if __name__ =='__main__':
    print(solution(48))