def solution(arr):
    l = len(arr)
    cnt = 0
    
    while l > 1:
        
        l /= 2
        cnt += 1
        
    return arr + [0] * (2**cnt-len(arr))

if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5, 6]))
    print(solution([58, 172, 746, 89]))