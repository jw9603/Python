def solution(age):
    
    return ''.join([chr(int(i)+97) for i in str(age)])

if __name__ =='__main__':
    print(solution(23))
    print(solution(51))
    print(solution(100))