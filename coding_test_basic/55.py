def solution(cipher, code):
    answer = ''
    for i in range(code,len(cipher)+1):
        if i % code == 0:
            answer +=cipher[i-1]
    return answer

if __name__ =='__main__':
    print(solution("dfjardstddetckdaccccdegk",4))