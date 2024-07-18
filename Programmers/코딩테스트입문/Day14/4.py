def solution(my_string):
    answer = ''
    for i in my_string:
        if i.islower():
            answer += i.upper()
        else:
            answer += i.lower()
    return answer

if __name__ == '__main__':
    print(solution("cccCCC"))
    print(solution("abCdEfghIJ"))