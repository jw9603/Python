def solution(keyinput, board):
    answer = [0,0] # answer[0] : 가로, answer[1] : 세로
    w = board[0]
    h = board[1]
    for i in keyinput: # ex) w = 9, h=9
        if i == 'left' and -(w // 2) + 1 <= answer[0]:  
            answer[0] -= 1
        elif i == 'right' and w // 2 - 1 >= answer[0]:
                answer[0] += 1
        elif i == 'up' and h // 2 - 1 >= answer[1]:
            answer[1] += 1
            
        elif i == 'down' and -(h // 2) + 1 <= answer[1]:
            answer[1] -= 1 
        
    return answer

if __name__ == '__main__':
    print(solution(["left", "right", "up", "right", "right"],[11,11]))
    print(solution(["down", "down", "down", "down", "down"],[7,9]))