def solution(arr):
    
    index = [i for i,x in enumerate(arr) if x == 2]
    return arr[min(index):max(index)+1] if index != [] else [-1]

if __name__ == '__main__':
    print(solution([1, 2, 1, 4, 5, 2, 9]))
    print(solution([1,2,1]))
    print(solution([1,1,1]))
    print(solution([1, 2, 1, 2, 1, 10, 2, 1]))