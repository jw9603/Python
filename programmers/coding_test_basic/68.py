def solution(quiz):
    return ["O" if eval(i.split('=')[0]) == int(i.split('=')[1]) else "X" for i in quiz]

if __name__ =='__main__':
    print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))