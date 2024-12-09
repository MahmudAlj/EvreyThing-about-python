import math
import copy
import time

def initialize_board():
    board = [[" "] * 8 for _ in range(8)]
    black_positions = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    for x, y in black_positions:
        board[x][y] = "0"

    white_positions = [(5, 5), (5, 6), (5, 7), (6, 5), (6, 6), (6, 7), (7, 5), (7, 6), (7, 7)]
    for x, y in white_positions:
        board[x][y] = "O"
    return board

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_goal_state(board, player):
    target_positions = [(7, 7), (7, 6), (7, 5), (6, 7), (6, 6), (6, 5), (5, 7), (5, 6), (5, 5)] if player == "0" else \
                        [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    return all(board[x][y] == player for x, y in target_positions)

def is_valid_move(board, player, start, end):
    sx, sy = start
    ex, ey = end

    if not (0 <= sx < 8 and 0 <= sy < 8 and 0 <= ex < 8 and 0 <= ey < 8):
        return False

    if board[sx][sy] != player:
        return False

    if board[ex][ey] != " ":
        return False

    dx = abs(ex - sx)
    dy = abs(ey - sy)

    if (dx, dy) in [(1, 0), (0, 1), (1, 1)]:
        return True

    if (dx, dy) in [(2, 0), (0, 2), (2, 2)]:
        mx, my = (sx + ex) // 2, (sy + ey) // 2
        if board[mx][my] != " ":
            return True

    return False

def get_valid_moves(board, player):
    moves = []
    for x in range(8):
        for y in range(8):
            if board[x][y] == player:
                for dx in [-2, -1, 0, 1, 2]:
                    for dy in [-2, -1, 0, 1, 2]:
                        ex, ey = x + dx, y + dy
                        if is_valid_move(board, player, (x, y), (ex, ey)):
                            moves.append(((x, y), (ex, ey)))
    return moves

def make_move(board, start, end):
    sx, sy = start
    ex, ey = end
    board[ex][ey] = board[sx][sy]
    board[sx][sy] = " "

def evaluate_board(board, player):
    opponent = "O" if player == "0" else "0"
    target_positions = [(7, 7), (7, 6), (7, 5), (6, 7), (6, 6), (6, 5), (5, 7), (5, 6), (5, 5)] if player == "0" else \
                        [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

    def distance_to_goal(x, y):
        return min(abs(x - tx) + abs(y - ty) for tx, ty in target_positions)

    player_score = sum(-distance_to_goal(x, y) for x in range(8) for y in range(8) if board[x][y] == player)
    opponent_score = sum(-distance_to_goal(x, y) for x in range(8) for y in range(8) if board[x][y] == opponent)

    return player_score - opponent_score

def minimax(board, depth, is_maximizing, player, alpha, beta, visited):
    board_tuple = tuple(tuple(row) for row in board)
    if board_tuple in visited:
        return -math.inf, None
    visited.add(board_tuple)

    if depth == 0 or is_goal_state(board, player):
        return evaluate_board(board, player), None

    valid_moves = get_valid_moves(board, player)
    if not valid_moves:
        return evaluate_board(board, player), None

    best_move = None
    opponent = "O" if player == "0" else "0"

    if is_maximizing:
        max_eval = -math.inf
        for move in valid_moves:
            new_board = copy.deepcopy(board)
            make_move(new_board, move[0], move[1])
            eval, _ = minimax(new_board, depth - 1, False, opponent, alpha, beta, visited)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = math.inf
        for move in valid_moves:
            new_board = copy.deepcopy(board)
            make_move(new_board, move[0], move[1])
            eval, _ = minimax(new_board, depth - 1, True, opponent, alpha, beta, visited)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def play_game(agent1_depth, agent2_depth):
    board = initialize_board()
    current_player = "0"
    visited = set()
    while True:
        print_board(board)
        if current_player == "0":
            _, best_move = minimax(board, agent1_depth, True, current_player, -math.inf, math.inf, visited)
        else:
            _, best_move = minimax(board, agent2_depth, True, current_player, -math.inf, math.inf, visited)

        if best_move:
            make_move(board, best_move[0], best_move[1])
            if is_goal_state(board, current_player):
                print(f"Player {current_player} wins!")
                break
            current_player = "O" if current_player == "0" else "0"
        else:
            print("No valid moves. Game over!")
            break

if __name__ == "__main__":
    play_game(3, 2)
