# 백준 2580. 스도쿠
# https://www.acmicpc.net/problem/2580

# 각각의 가로줄과 세로줄에는 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
# 굵은 선으로 구분되어 있는 3x3 정사각형 안에도 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
def dfs(index):

    if index == len(empty_cells):
        for row in board:
            print(' '.join(map(str, row)))
        return True

    r, c = empty_cells[index]
    box_idx = (r // 3) * 3 + (c // 3)

    for num in range(1, 10):
        if num not in rows[r] and num not in cols[c] and num not in boxes[box_idx]:
            board[r][c] = num
            rows[r].add(num)
            cols[c].add(num)
            boxes[box_idx].add(num)

            if dfs(index + 1):
                return True
            
            board[r][c] == 0
            rows[r].remove(num)
            cols[c].remove(num)
            boxes[box_idx].remove(num)

def main():
    global board, rows, cols, boxes, empty_cells
    board = [list(map(int, input().split())) for _ in range(9)]

    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empty_cells = []

    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                empty_cells.append((r, c))
            else:
                num = board[r][c]
                rows[r].add(num)
                cols[c].add(num)
                boxes[(r // 3) * 3 + (c // 3)].add(num)
    
    dfs(0)

if __name__ == '__main__':
    main()