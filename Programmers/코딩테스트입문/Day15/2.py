def solution(my_string, num1, num2):
    my_string = list(my_string)
    my_string[num1],my_string[num2] = my_string[num2],my_string[num1]
    
    return ''.join(my_string)

if __name__ == '__main__':
    print(solution("hello",1,2))
    print(solution("I love you",3,6))