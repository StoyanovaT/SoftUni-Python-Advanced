def find_player_position(matrix, player):
    player_position = ()
    for row in range(8):
        for col in range(8):
            if matrix[row][col] == player:
                player_position = (row, col)

    return player_position


def get_cell_name(row, col):
    rows_name = [8, 7, 6, 5, 4, 3, 2, 1]
    col_name = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    return rows_name[row], col_name[col]


ROWS_COUNT = 8
COLUMNS_COUNT = 8

matrix = [input().split(' ') for _ in range(ROWS_COUNT)]

current_player = 'w'
other_player = 'b'
current_player_position = find_player_position(matrix, 'w')
other_player_position = find_player_position(matrix, 'b')
current_delta = -1
other_delta = +1

is_capture = False
is_queen = False

while True:
    current_player_row, current_player_col = current_player_position
    other_player_row, other_player_col = other_player_position
    current_player_row += current_delta
    current_player_position = (current_player_row, current_player_col)

    if current_player_row == other_player_row and abs(current_player_col - other_player_col) == 1:
        is_capture = True
        current_player_col = other_player_col
        current_player_position = (current_player_row, other_player_col)
        break

    elif current_player_row in (0, ROWS_COUNT - 1):
        is_queen = True
        break

    else:
        current_player, other_player = other_player, current_player
        current_delta, other_delta = other_delta, current_delta
        current_player_position, other_player_position = other_player_position, current_player_position

winner = 'White' if current_player == 'w' else "Black"
(row_name, col_name) = get_cell_name(*current_player_position)
winning_cell_name = f'{col_name}{row_name}'

if is_capture:
    print(f"Game over! {winner} win, capture on {winning_cell_name}.")
else:
    print(f"Game over! {winner} pawn is promoted to a queen at {winning_cell_name}.")
