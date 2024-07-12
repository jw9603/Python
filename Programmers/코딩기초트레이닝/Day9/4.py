def solution(my_string):
    return sorted(my_string[i:] for i in range(len(my_string)))

if __name__ =='__main__':
    print(solution('banana'))
    print(solution("programmers"))