def solution(quiz):
    answer = []
    for i in quiz:
        if eval(i[:i.index('=')]) == int(i[i.index('=')+1:].strip()):
            answer.append('O')
        else:
            answer.append('X')
    return answer

if __name__ == '__main__':
    print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
    print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))