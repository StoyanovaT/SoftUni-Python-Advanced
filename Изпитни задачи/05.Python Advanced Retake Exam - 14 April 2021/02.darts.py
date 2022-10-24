def is_outside(row, col, size):
    return row < 0 or row >= size or col < 0 or col >= size


def get_corresponding(row, col, matrix):
    result = sum([int(matrix[row][0]), int(matrix[row][6]), int(matrix[0][col]), int(matrix[6][col])])
    return result


size = 7

cur_player, next_player = input().split(', ')
cur_player_turn = 0
next_player_turn = 0
cur_player_points = 501
next_player_points = 501

matrix = [[x for x in input().split()] for _ in range(size)]

while True:
    cords = input().strip('()')
    row, col = [int(x) for x in cords.split(', ')]

    cur_player_turn += 1

    if is_outside(row, col, size):
        cur_player, next_player = next_player, cur_player
        cur_player_turn, next_player_turn = next_player_turn, cur_player_turn
        cur_player_points, next_player_points = next_player_points, cur_player_points
        continue

    if matrix[row][col] == "B":
        break

    if matrix[row][col] == "D" or matrix[row][col] == "T":
        corresponding_sum = get_corresponding(row, col, matrix)
        if matrix[row][col] == "D":
            cur_player_points -= corresponding_sum * 2
        else:
            cur_player_points -= corresponding_sum * 3

    else:
        cur_player_points -= int(matrix[row][col])

    if cur_player_points <= 0:
        break

    cur_player, next_player = next_player, cur_player
    cur_player_turn, next_player_turn = next_player_turn, cur_player_turn
    cur_player_points, next_player_points = next_player_points, cur_player_points

print(f"{cur_player} won the game with {cur_player_turn} throws!")