def solution(keyinput, board):
    col = board[0]
    row = board[1]
    result = [0, 0]
    for i in keyinput:
        if i == "left" and result[0]-1 >= -(col // 2):
            result[0] -= 1
        elif i == "right" and result[0]+1 <= (col // 2):
            result[0] += 1
        elif i == "up" and result[1]+1 <= (row // 2):
            result[1] += 1
        elif i == "down" and result[1]-1 >= -(row // 2):
            result[1] -= 1
    return result

if __name__ =='__main__':
    print(solution(["left", "right", "up", "right", "right"],[11, 11]))