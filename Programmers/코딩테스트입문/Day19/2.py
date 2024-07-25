def solution(my_str, n):
    
    return [my_str[i:i+n] for i in range(0,len(my_str),n)]

if __name__ == '__main__':
    print(solution("abc1Addfggg4556b",6))
    print(solution("abcdef123",3))