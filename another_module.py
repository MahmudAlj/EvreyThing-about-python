import heapq

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def is_valid_move(board, row, col, num):
    for x in range(9):
        if board[row][x] == num:
            return False
    for x in range(9):
        if board[x][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True


def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def heuristic_cost(board):
    return sum(row.count(0) for row in board)


def a_star_solver(board):
    open_list = []
    visited = set()
    initial_heuristic = heuristic_cost(board)
    heapq.heappush(open_list, (initial_heuristic, 0, board))  # (f(n), g(n), board)

    steps = 0

    while open_list:
        f, g, current_board = heapq.heappop(open_list)
        board_tuple = tuple(tuple(row) for row in current_board)
        if board_tuple in visited:
            continue
        visited.add(board_tuple)

        empty = find_empty_cell(current_board)

        if not empty:
            print(f"Solution found in {steps} steps.")
            return current_board

        row, col = empty
        for num in range(1, 10):
            if is_valid_move(current_board, row, col, num):
                new_board = [r[:] for r in current_board]
                new_board[row][col] = num
                new_g = g + 1
                new_f = new_g + heuristic_cost(new_board)  # f(n) = g(n) + h(n)
                heapq.heappush(open_list, (new_f, new_g, new_board))
                steps += 1

    print("No solution found.")
    return None


def start_game(board):
    print("Starting Sudoku Solver...")
    solution = a_star_solver(board)
    if solution:
        print("Solved by AI:")
        print_board(solution)
    else:
        print("AI couldn't solve the puzzle.")

board = [
    [0, 0, 9, 0, 0, 0, 0, 0, 2],
    [8, 7, 5, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 3, 0, 9],
    [0, 0, 0, 0, 0, 0, 7, 0, 0],
    [0, 0, 0, 5, 0, 7, 0, 9, 0],
    [1, 0, 0, 8, 0, 0, 5, 0, 0],
    [4, 0, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 0, 4, 6],
    [0, 8, 0, 0, 1, 0, 0, 0, 0]
]

start_game(board)
