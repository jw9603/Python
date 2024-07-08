def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a + d*i) * int(included[i])
    return answer

if __name__ == '__main__':
    print(solution(3,4,['true', 'false', 'false', 'true', 'true']))
    print(solution(7,1,['false', 'false', 'false', 'true', 'false', 'false', 'false']))