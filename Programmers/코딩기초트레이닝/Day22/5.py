def solution(my_string, target):
    
    return int(target in my_string)

if __name__ == '__main__':
    print(solution("banana",'ana'))
    print(solution("banana","wxyz"))