def solution(rsp):
    answer = ''
    rsp = list(rsp)
    for i in rsp:
        if i == '2':
            answer += '0'
        elif i == '0':
            answer += '5'
        else:
            answer += '2'
    return answer

######### 다른 풀이 #############
# def solution(rsp):
#     d = {"2":"0","0":"5","5":"2"}
#     return ''.join(d[i] for i in rsp)
######### 다른 풀이 #############
if __name__ =='__main__':
    print(solution("2"))
    print(solution("205"))