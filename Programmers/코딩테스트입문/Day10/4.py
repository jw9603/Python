from collections import deque
def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
     
    else:
        numbers.rotate(-1)

    return list(numbers)

if __name__ == '__main__':
    print(solution([1,2,3],"right"))
    print(solution([4, 455, 6, 4, -1, 45, 6],"left"))