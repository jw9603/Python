def solution(n):
    answer = [n]
    while n!= 1:
        if n%2 == 0:
            n /= 2

        else:
            n = 3 * n + 1
        answer.append(n)
    return answer

if __name__ =='__main__':
    print(solution(10))