def solution(q, r, code):
    answer = ''
    for i in range(len(code)):
        if i % q == r:
            answer += code[i]
    return answer

if __name__ == '__main__':
    print(solution(3,1,"qjnwezgrpirldywt"))
    print(solution(1,0,"programmers"))