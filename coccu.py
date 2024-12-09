import numpy as np
import pygame as p
import pygame.time


# --- Game Engine Code ---
class GameState():
    def __init__(self):
        self.board = np.array([
            ["--", "--", "--", "--", "--", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "--", "--", "--", "--", "--"]
        ])

        self.whiteToMove = True
        self.moveLog = []
        self.gameOver = False

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"  # the square the piece left becomes empty
        self.board[move.endRow][move.endCol] = move.pieceMoved  # the square the piece arrives at
        self.moveLog.append(move)  # logging the move
        self.isTheGameOver()
        if self.gameOver:
            pass
        else:
            self.whiteToMove = not self.whiteToMove  # change turn

    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved  # take the piece back to its position
            self.board[move.endRow][move.endCol] = "--"  # remove the piece in the position we put it in
            self.whiteToMove = not self.whiteToMove
            self.gameOver = False

    def getAllPossibleMoves(self):  # All legal moves
        moves = []

        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                pieceColor = self.board[r][c][0]
                if (pieceColor == 'w' and self.whiteToMove) or (pieceColor == 'b' and not self.whiteToMove):
                    self.getMoves(r, c, moves)

        return moves

    def getMoves(self, r, c, moves):  # All legal moves of a specific piece
        if self.whiteToMove:  # white pieces
            try:  # Move up
                if self.board[r - 1][c] == "--":
                    moves.append(Move((r, c), (r - 1, c), self.board))
            except IndexError:
                pass

            try:  # Move right
                if self.board[r][c + 1] == "--":
                    moves.append(Move((r, c), (r, c + 1), self.board))
            except IndexError:
                pass

            if (0 <= r <= 2) and (5 <= c <= 7):  # Checking if we can move backwards (if we are in opponents squares)
                if self.board[r + 1][c] == "--" and (0 <= r + 1 <= 2):
                    moves.append(Move((r, c), (r + 1, c), self.board))
                if self.board[r][c - 1] == "--" and (5 <= c - 1 <= 7):
                    moves.append(Move((r, c), (r, c - 1), self.board))
            self.getJumpingMoves(r, c, moves, (r, c))

        else:  # black pieces
            try:  # Move down
                if self.board[r + 1][c] == "--":
                    moves.append(Move((r, c), (r + 1, c), self.board))
            except IndexError:
                pass

            try:  # Move left
                if self.board[r][c - 1] == "--":
                    moves.append(Move((r, c), (r, c - 1), self.board))
            except IndexError:
                pass

            if (5 <= r <= 7) and (0 <= c <= 2):  # Checking if we can move backwards (if we are in opponents squares)
                if self.board[r - 1][c] == "--" and (5 <= r - 1 <= 7):
                    moves.append(Move((r, c), (r - 1, c), self.board))
                if self.board[r][c + 1] == "--" and (0 <= c + 1 <= 2):
                    moves.append(Move((r, c), (r, c + 1), self.board))
            self.getJumpingMoves(r, c, moves, (r, c))

    def getJumpingMoves(self, r, c, moves, originalSquare):  # Calculating legal moves where we jump on top of pieces.
        startRow = originalSquare[0]
        startCol = originalSquare[1]
        if self.whiteToMove:  # white pieces
            try:
                if self.board[r - 1][c] != "--" and self.board[r - 2][c] == "--":  # Checking if we can jump
                    moves.append(Move((startRow, startCol), (r - 2, c), self.board))
                    self.getJumpingMoves(r - 2, c, moves, originalSquare)  # Recursion
            except IndexError:
                pass

            try:
                if self.board[r][c + 1] != "--" and self.board[r][c + 2] == "--":  # Checking the other direction
                    moves.append(Move((startRow, startCol), (r, c + 2), self.board))
                    self.getJumpingMoves(r, c + 2, moves, originalSquare)
            except IndexError:
                pass

        else:  # black pieces
            try:
                if self.board[r + 1][c] != "--" and self.board[r + 2][c] == "--":  # Checking if we can jump
                    moves.append(Move((startRow, startCol), (r + 2, c), self.board))
                    self.getJumpingMoves(r + 2, c, moves, originalSquare)  # Recursion
            except IndexError:
                pass

            try:
                if self.board[r][c - 1] != "--" and self.board[r][c - 2] == "--":  # Checking the other direction
                    moves.append(Move((startRow, startCol), (r, c - 2), self.board))
                    self.getJumpingMoves(r, c - 2, moves, originalSquare)  # Recursion
            except IndexError:
                pass

    def isTheGameOver(self):
        count = 0
        if self.whiteToMove:
            for i in range(0, 3):
                for j in range(5, 8):
                    if self.board[i][j] == "wp":
                        count += 1

        else:
            for i in range(5, 8):
                for j in range(0, 3):
                    if self.board[i][j] == "bp":
                        count += 1

        if count == 9:
            self.gameOver = True


class Move:
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSquare, endSquare, board):
        self.startRow = startSquare[0]
        self.startCol = startSquare[1]
        self.endRow = endSquare[0]
        self.endCol = endSquare[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.movID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol * 1

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.movID == other.movID
        else:
            return False

    def getNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]


# --- Pygame UI Code ---
WIDTH = HEIGHT = 512
DIMENSION = 8
SQUARE_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}


def loadImages():
    pieces = ["wp", "bp"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))

    gs = GameState()
    validMoves = gs.getAllPossibleMoves()
    moveMade = False
    animate = False

    loadImages()
    running = True

    squareSelected = ()
    playerClicks = []
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                if not gs.gameOver:
                    location = p.mouse.get_pos()
                    col = location[0] // SQUARE_SIZE
                    row = location[1] // SQUARE_SIZE

                    if squareSelected == (row, col):
                        squareSelected = ()
                        playerClicks = []
                    else:
                        squareSelected = (row, col)
                        playerClicks.append(squareSelected)

                    if len(playerClicks) == 2:
                        move = gs.makeMove(Move(playerClicks[0], playerClicks[1], gs.board))
                        if move != "invalid":
                            moveMade = True
                        squareSelected = ()
                        playerClicks = []

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)


def drawBoard(screen):
    colors = [p.Color(255, 255, 255), p.Color(200, 200, 200)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


if __name__ == "__main__":
    main()
