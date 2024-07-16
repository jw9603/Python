def solution(n, slicer, num_list):

    if n == 1:
        return num_list[:slicer[1]+1]
    elif n == 2:
        return num_list[slicer[0]:]
    elif n == 3:
        return num_list[slicer[0]:slicer[1]+1]
    else:
        return num_list[slicer[0]:slicer[1]+1:slicer[-1]]
    
if __name__ == '__main__':
    print(solution(3,[1,5,2],[1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(solution(4,[1,5,2],[1, 2, 3, 4, 5, 6, 7, 8, 9]))