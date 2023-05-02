def solution(array, height):
    
    return len([array[i] for i in range(len(array)) if array[i] > height])

if __name__ =='__main__':
    print(solution([180, 120, 140],190))