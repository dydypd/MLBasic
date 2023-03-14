"""
Thông tin nhóm
Phạm Đức Duy, 20000536, K65TT
Bùi Đức Duy, 20000534, K65TT
Nguyễn Đăng Dương, 20000538, K65TT

Danh sách bài tập
- Bài 1. get_all_coords(), get_white_coords(), print_broad()
- Bài 2. get_random()
- Bài 3. list_filtered()
- Bài 4. queen_moves()
- Bài 5. fen_to_coords()
"""
import itertools
import random
import chess


def get_all_coords():
    files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    ranks = range(1, 9)
    return [f"{file}{rank}" for rank in ranks for file in files]


def get_white_coords():
    all_coords = get_all_coords()
    white_coords = []
    for coord in all_coords:
        file, rank = coord[0], int(coord[1])
        if (rank % 2 == 0 and ord(file) % 2 != 0) or (rank % 2 != 0 and ord(file) % 2 == 0):
            white_coords.append(coord)
    return white_coords


def print_board():
    ranks = range(8, 0, -1)
    files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    rows = [list(itertools.islice(get_all_coords(), i - 8, i)) for i in range(64, 0, -8)]
    for rank, row in zip(ranks, rows):
        print(" ".join(row))


def get_random(input_list):
    # Lấy 1 chỉ số bất kỳ từ 0 đến input_list size
    random_index = random.randint(0, len(input_list))
    return input_list[random_index]


def list_filtered(A, B):
    C = [a for a in A if a not in B]
    return C


def queen_moves(position):
    column, row = position

    # Tìm các ô trên cùng hàng
    moves = [chr(i) + row for i in range(ord('a'), ord('h') + 1) if chr(i) != column]

    # Tìm các ô trên cùng cột
    moves += [column + str(i) for i in range(1, 9) if str(i) != row]

    # Tìm các ô trên cùng đường chéo
    diagonal1 = [chr(i) + str(j) for i, j in zip(range(ord(column) - 1, ord('a') - 1, -1), range(int(row) - 1, 0, -1))]
    diagonal2 = [chr(i) + str(j) for i, j in zip(range(ord(column) + 1, ord('h') + 1), range(int(row) - 1, 0, -1))]
    diagonal3 = [chr(i) + str(j) for i, j in zip(range(ord(column) - 1, ord('a') - 1, -1), range(int(row) + 1, 9))]
    diagonal4 = [chr(i) + str(j) for i, j in zip(range(ord(column) + 1, ord('h') + 1), range(int(row) + 1, 9))]

    moves += diagonal1 + diagonal2 + diagonal3 + diagonal4

    # Xóa các ô trùng nhau
    moves = list(set(moves))

    # Sắp xếp lại các ô theo thứ tự từ trái qua phải, từ trên xuống dưới
    moves.sort(key=lambda x: (ord(x[0]), int(x[1])))

    return moves


def fen_to_coords(fen):
    board = chess.Board(fen)
    return board


# Test bài 1
print(get_all_coords())
print(get_white_coords())
print_board()
# Test bài 2
get_random(['a', 'b', 'c', 'd'])
# Test bài 3
A = [1, 2, 3, 4, 5, 8, 9]
B = [2, 3, 4, 5, 6, 7]
print(list_filtered(A, B))
# Test bài 4
print(queen_moves('a3'))
# Test bài 5
fen = "r1bqkbnr/pppp1ppp/2n5/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 1 2"
board = fen_to_coords(fen)
print(board)
