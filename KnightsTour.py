# Chessboard 5x5 visualization
# [0,0][1,0][2,0][3,0][4,0]
# [0,1][1,1][2,1][3,1][4,1]
# [0,2][1,2][2,2][3,2][4,2]
# [0,3][1,3][2,3][3,3][4,3]
# [0,4][1,4][2,4][3,4][4,4]

# Possible moves for a knight
knight_moves = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

def is_valid(x, y, board, M, N):
    return 0 <= x < M and 0 <= y < N and board[x][y] == -1

def knights_tour(board, x, y, move_count, M, N, moves):
    if move_count == M * N:
        return True

    for move in knight_moves:
        next_x, next_y = x + move[0], y + move[1]
        if is_valid(next_x, next_y, board, M, N):
            board[next_x][next_y] = move_count
            moves.append((next_x, next_y))
            if knights_tour(board, next_x, next_y, move_count + 1, M, N, moves):
                return True
            board[next_x][next_y] = -1
            moves.pop()
    return False

def start_knights_tour(M, N, start_x, start_y):
    board = [[-1 for _ in range(N)] for _ in range(M)]

    board[start_x][start_y] = 0
    moves = [(start_x, start_y)]

    if knights_tour(board, start_x, start_y, 1, M, N, moves):
        for move in moves:
            print(f"{move[0]} {move[1]}")
    else:
        print("No solution found")

M = int(input("Enter the Number of rows chessboard: "))
N = int(input("Enter the Number of columns chessboard: "))
start_x, start_y = map(int, input("Enter the starting position of the knight (x y): ").split())

start_knights_tour(M, N, start_x, start_y)
