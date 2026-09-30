def is_valid(board, row, col, num):
    
    for c in range(4):
        if board[row][c] == num:
            return False
    
    for r in range(4):
        if board[r][col] == num:
            return False
    
    br = (row // 2) * 2
    bc = (col // 2) * 2
    for r in range(br, br + 2):
        for c in range(bc, bc + 2):
            if board[r][c] == num:
                return False
    return True


def solve_sudoku(matrix):
    """
    Рекурсивно решает мини-судоку 4x4.
    Возвращает True, если решение найдено (матрица изменяется на месте).
    """
    for row in range(4):
        for col in range(4):
            if matrix[row][col] == 0:
                for num in range(1, 5):
                    if is_valid(matrix, row, col, num):
                        matrix[row][col] = num
                        if solve_sudoku(matrix):
                            return True
                        matrix[row][col] = 0  # откат
                return False
    return True  


if __name__ == "__main__":
    board = [
        [0, 0, 0, 0],
        [0, 0, 2, 0],
        [0, 1, 0, 0],
        [3, 0, 0, 4],
    ]
    if solve_sudoku(board):
        for row in board:
            print(row)
    else:
        print("Решения нет")