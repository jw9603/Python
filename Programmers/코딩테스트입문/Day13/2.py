def solution(strlist):
    return [len(i) for i in strlist]

if __name__ == '__main__':
    print(solution(["We", "are", "the", "world!"]))
    print(solution(["I", "Love", "Programmers."]))