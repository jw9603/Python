def solution(n):

    return 1 if n ** 0.5 == int(n**0.5) else 2

if __name__ =='__main__':
    print(solution(144))
    print(solution(145))