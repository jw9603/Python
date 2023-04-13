def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer +=i
    return answer

if __name__=='__main__':
    print(solution("We are the world"))