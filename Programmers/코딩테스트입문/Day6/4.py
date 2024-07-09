def solution(my_string, n):
    
    return ''.join([i*n for i in my_string])

if __name__ =='__main__':
    print(solution('hello',3))