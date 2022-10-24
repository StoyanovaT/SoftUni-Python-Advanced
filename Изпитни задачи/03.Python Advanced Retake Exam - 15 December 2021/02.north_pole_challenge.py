def get_next_position(row, col, direction_to_go, row_s, col_s):
    next_r = 0
    next_c = 0
    if direction_to_go == 'left':
        if col == 0:
            next_r = row
            next_c = col_s - 1
        else:
            next_r = row
            next_c = col - 1

    elif direction_to_go == 'right':
        if col == col_s - 1:
            next_r = row
            next_c = 0
        else:
            next_r = row
            next_c = col + 1

    elif direction_to_go == 'up':
        if row == 0:
            next_r = row_s - 1
            next_c = col
        else:
            next_r = row - 1
            next_c = col

    elif direction_to_go == 'down':
        if row == row_s - 1:
            next_r = 0
            next_c = col
        else:
            next_r = row + 1
            next_c = col

    return next_r, next_c


def check_if_outside(row, col, r_size, c_size):
    return 0 < row >= r_size and 0 < col >= c_size


row_size, col_size = [int(x) for x in input().split(', ')]
player_row = 0
player_col = 0
decorations = 0
gifts = 0
cookies = 0
matrix = []
collected_dict = {'D': 0, 'G': 0, 'C': 0}

for row_index in range(row_size):
    row_elements = input().split()
    for col_index in range(col_size):
        if row_elements[col_index] == "Y":
            player_row = row_index
            player_col = col_index
        elif row_elements[col_index] == "D":
            decorations += 1
        elif row_elements[col_index] == "G":
            gifts += 1
        elif row_elements[col_index] == "C":
            cookies += 1
    matrix.append(row_elements)

items_to_collect = decorations + gifts + cookies

while items_to_collect > 0:
    command = input()
    if command == "End":
        break

    direction, steps = command.split('-')
    steps = int(steps)

    matrix[player_row][player_col] = 'x'

    for _ in range(steps):
        next_row, next_col = get_next_position(player_row, player_col, direction, row_size, col_size)
        player_row, player_col = next_row, next_col

        if matrix[player_row][player_col] == '.':
            matrix[player_row][player_col] = 'x'
            continue

        if matrix[player_row][player_col] == 'x':
            continue

        if matrix[player_row][player_col] == 'D':
            collected_dict['D'] += 1

        if matrix[player_row][player_col] == 'G':
            collected_dict['G'] += 1

        if matrix[player_row][player_col] == 'C':
            collected_dict['C'] += 1

        items_to_collect -= 1
        if items_to_collect == 0:
            break
        matrix[player_row][player_col] = 'x'

matrix[player_row][player_col] = 'Y'
collected_values = [value for _, value in collected_dict.items()]

if items_to_collect == 0:
    print("Merry Christmas!")
print("You've collected:")
print(f"- {collected_values[0]} Christmas decorations")
print(f"- {collected_values[1]} Gifts")
print(f"- {collected_values[2]} Cookies")
for row in matrix:
    print(*row)

