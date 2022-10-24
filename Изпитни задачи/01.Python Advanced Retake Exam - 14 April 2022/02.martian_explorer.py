from collections import deque


def get_next_position(row, col, direction):
    if direction == 'up':
        return row - 1, col
    elif direction == 'down':
        return row + 1, col
    elif direction == 'left':
        return row, col - 1
    elif direction == 'right':
        return row, col + 1


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def deposit_collect_and_print(row, col, matrix):
    if matrix[row][col] in 'WMC':
        if matrix[row][col] == 'W':
            deposits_collected['Water'] += 1
            print(f"Water deposit found at ({row}, {col})")
        elif matrix[row][col] == 'M':
            deposits_collected['Metal'] += 1
            print(f"Metal deposit found at ({row}, {col})")
        elif matrix[row][col] == 'C':
            deposits_collected['Concrete'] += 1
            print(f"Concrete deposit found at ({row}, {col})")
        matrix[row][col] = '-'

def check_for_rock(row, col, matrix):
    if matrix[row][col] == 'R':
        print(f"Rover got broken at ({next_row}, {next_col})")
        return 'Crashed'


size = 6
matrix = []
rover_row = 0
rover_col = 0

deposits_collected = {'Water': 0, 'Metal': 0, 'Concrete': 0}

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 'E':
            rover_row = row
            rover_col = col
    matrix.append(row_elements)

commands = deque(input().split(', '))

while commands:
    direction = commands.popleft()

    next_row, next_col = get_next_position(rover_row, rover_col, direction)

    if not is_inside(next_row, next_col, size):
        if next_row > 5:
            next_row = 0
        elif next_row < 0:
            next_row = 5

        if next_col > 5:
            next_col = 0
        elif next_col < 0:
            next_col = 5
        deposit_collect_and_print(next_row, next_col, matrix)
        rover_row = next_row
        rover_col = next_col
        if check_for_rock(rover_row, rover_col, matrix) == 'Crashed':
            break
        continue

    if check_for_rock(next_row, next_col, matrix) == 'Crashed':
        break

    else:
        rover_row = next_row
        rover_col = next_col

        if matrix[rover_row][rover_col] == '-':
            continue

        deposit_collect_and_print(rover_row, rover_col, matrix)


if 0 in deposits_collected.values():
    print("Area not suitable to start the colony.")
else:
    print("Area suitable to start the colony.")
