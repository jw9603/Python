def solution(numbers):
    
    return max([numbers[i] * numbers[j] for i in range(len(numbers)) for j in range(i+1,len(numbers))])

if __name__=='__main__':
    print(solution([10, 20, 30, 5, 5, 20, 5]))