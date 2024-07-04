def solution(array):
    return sorted(array)[len(array)//2]

if __name__ == '__main__':
    print(solution([1,2,7,19,-1]))