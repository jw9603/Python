def solution(code):
    answer = ''

    mode = 0
    for i in range(len(code)):
        if mode == 0:
            if code[i] == '1':
                mode = 1
            else:
                if i % 2 == mode:
                    answer += code[i]
        else:
            if code[i] == '1':
                mode = 0
            else:
                if i%2 == mode:
                    answer += code[i]

    return answer if answer else 'EMPTY'

if __name__ =='__main__':
    print(solution("abc1abc1abc"))