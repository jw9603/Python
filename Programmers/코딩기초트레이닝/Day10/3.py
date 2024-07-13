def solution(my_string, s, e):
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]

if __name__ == '__main__':
    print(solution("Progra21Sremm3",6,12))
    print(solution("Stanley1yelnatS",4,10))