import heapq
#buna bırde rastgale sayılar ıle cozen bır sey yapıp gıthaba at
def sudoko(s_tahta):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(s_tahta[i][j])
            else:
                print(str(s_tahta[i][j]) + " ", end="")



def tahtadeger(s_tahta, row, col, num):
    for x in range(9):
        if s_tahta[row][x] == num:
            return False
    for x in range(9):
        if s_tahta[x][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if s_tahta[i + start_row][j + start_col] == num:
                return False
    return True


def bos_deger_bul(s_tahta):
    for i in range(9):
        for j in range(9):
            if s_tahta[i][j] == 0:
                return (i, j)
    return None


def heuristic(s_tahta):
    return sum(row.count(0) for row in s_tahta)


def a_star_sudoku(s_tahta):
    open_list = []
    visited = set()
    initial_heuristic = heuristic(s_tahta)
    heapq.heappush(open_list, (initial_heuristic, 0, s_tahta))  # (f(n), g(n), s_tahta)

    steps = 0

    while open_list:
        f, g, gidis_s_tahta = heapq.heappop(open_list)
        s_tahta_tuple = tuple(tuple(row) for row in gidis_s_tahta)
        if s_tahta_tuple in visited:
            continue
        visited.add(s_tahta_tuple)

        empty = bos_deger_bul(gidis_s_tahta)

        if not empty:
            print(f"{steps} adimda bulundu.")
            return gidis_s_tahta

        row, col = empty
        for num in range(1, 10):
            if tahtadeger(gidis_s_tahta, row, col, num):
                yeni_s_tahta = [row[:] for row in gidis_s_tahta]
                yeni_s_tahta[row][col] = num
                yeni_g = g + 1
                yeni_f = yeni_g + heuristic(yeni_s_tahta)  # f(n) = g(n) + h(n)
                heapq.heappush(open_list, (yeni_f, yeni_g, yeni_s_tahta))
                steps += 1

    print("cozum bulmadi.")
    return None


def play_sudoku(s_tahta):
            solution = a_star_sudoku(s_tahta)
            if solution:
                print("robot cozdu:")
                sudoko(solution)
            else:
                print("robot cozemedi.")

s_tahta = [
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
play_sudoku(s_tahta)
