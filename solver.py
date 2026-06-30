
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def get_row(board: list[list[int]], row: int) -> list[int]:
    return board[row]

def get_col(board: list[list[int]], col: int) -> list[int]:
    return [row[col] for row in board]

def get_box(board: list[list[int]], row: int, col: int) -> list[list[int]]:
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    return [row_list[start_col:start_col + 3] for row_list in board[start_row:start_row + 3]]

def is_row_col_valid(row: list[int]) -> bool:
    if len(row) != len(set(row)):
        return False
    for number in row:
        if not number in nums:
            return False
    return True

def is_box_valid(box: list[list[int]]) -> bool:
    flat_box = [number for row in box for number in row]
    return is_row_col_valid(flat_box)

def is_solved(board) -> bool:
    for i in range(9):
        if not is_row_col_valid(get_row(board, i)):
            return False
        if not is_row_col_valid(get_col(board, i)):
            return False
    for row in range(3):
        for col in range(3):
            if not is_box_valid(get_box(board, row * 3, col * 3)):
                return False
    return True

def main():

    board = [
        [0, 1, 0,   0, 0, 0,   0, 0, 0],
        [2, 0, 0,   0, 0, 0,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 0],

        [0, 0, 0,   0, 0, 0,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 0],

        [0, 0, 0,   0, 0, 0,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 0],
        ]
    
    print(board[0])
    

if __name__ == '__main__':
    main()