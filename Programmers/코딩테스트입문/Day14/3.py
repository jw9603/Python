def solution(cipher, code):
    answer = ''
    for i in range(len(cipher)):
        if (i+1) % code ==0:
            answer += cipher[i]
        
    return answer

############## 다른 풀이 ##################
def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer
############## 다른 풀이 ##################

if __name__ == '__main__':
    print(solution("dfjardstddetckdaccccdegk",4))
    print(solution("pfqallllabwaoclk",2))