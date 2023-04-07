def solution(numbers, k):

    return numbers[2*(k-1)%len(numbers)]

# 이 문제 푸는데 시간 오래걸림

if __name__ =='__main__':
    print(solution([1,2,3,4,5,6],5))