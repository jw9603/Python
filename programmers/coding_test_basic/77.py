def solution(dots):
    
    return (max([dot[0] for dot in dots])-min([dot[0] for dot in dots])) * (max([dot[-1] for dot in dots])-min([dot[-1] for dot in dots]))

if __name__ =='__main__':
    print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))