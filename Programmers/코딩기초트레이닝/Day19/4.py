def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
        elif stk[-1] == arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])    
        i += 1
    return stk if stk else [-1]

if __name__ == '__main__':
    print(solution([0, 1, 1, 1, 0]))
    print(solution([0, 1, 0, 1, 0]))
    print(solution([0, 1, 1, 0]))