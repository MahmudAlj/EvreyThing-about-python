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


def is_valid(board, row, col, num):
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


def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def heuristic(board):
    return sum(row.count(0) for row in board)


def a_star_sudoku(board):
    open_list = []
    visited = set()
    initial_heuristic = heuristic(board)
    heapq.heappush(open_list, (initial_heuristic, 0, board))  # (f(n), g(n), board)

    steps = 0

    while open_list:
        f, g, current_board = heapq.heappop(open_list)
        board_tuple = tuple(tuple(row) for row in current_board)
        if board_tuple in visited:
            continue
        visited.add(board_tuple)

        empty = find_empty_location(current_board)

        if not empty:
            print(f"Çözüm {steps} adımda bulundu.")
            return current_board

        row, col = empty
        for num in range(1, 10):
            if is_valid(current_board, row, col, num):
                new_board = [row[:] for row in current_board]
                new_board[row][col] = num
                new_g = g + 1
                new_f = new_g + heuristic(new_board)  # f(n) = g(n) + h(n)
                heapq.heappush(open_list, (new_f, new_g, new_board))
                steps += 1

    print("Çözüm bulunamadı.")
    return None  # Çözüm bulunamadı


def play_sudoku(board):
    while True:
        print_board(board)
        choice = input("Bir sayı eklemek için 'e', Sudoku'yu yapay zeka çözsün için 'z' tuşlayın: ").lower()

        if choice == 'e':
            row = int(input("Satır numarası (1-9): ")) - 1
            col = int(input("Sütun numarası (1-9): ")) - 1
            num = int(input("Eklemek istediğiniz sayı (1-9): "))

            if is_valid(board, row, col, num):
                board[row][col] = num
                if not find_empty_location(board):
                    print("Tebrikler! Sudoku'yu başarıyla tamamladınız!")
                    print_board(board)
                    break
            else:
                print("Bu sayı burada kuralları ihlal ediyor. Başka bir sayı deneyin.")

        elif choice == 'z':
            solution = a_star_sudoku(board)
            if solution:
                print("Yapay zeka Sudoku'yu çözdü:")
                print_board(solution)
            else:
                print("Yapay zeka çözüm bulamadı.")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

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

print("Sudoku oyununa hoş geldiniz!")
play_sudoku(board)
