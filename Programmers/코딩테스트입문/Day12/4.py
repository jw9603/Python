def solution(n):
    answer = []
    i = 2
    while i <= n:
        if n % i == 0:
            answer.append(i)
            n //= i
        else:
            i += 1
            
    return sorted(list(set(answer)))

if __name__ == '__main__':
    print(solution(12.[2,3]))
    print(solution(17,[17]))
    print(solution(420,[2,3,5,7]))