def solution(number, n, m):
    return 1 if number % n ==0 and number % m ==0 else 0

if __name__ =='__main__':
    print(solution(60,2,3))
    print(solution(55,10,5))