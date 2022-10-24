matrix = [list(input())for _ in range(6)]
commands = input().split(", ")


def move_rover(row, col):
    if row > 5:
        row = 0
    elif row < 0:
        row = 5

    if col > 5:
        col = 0
    elif col < 0:
        col = 5

    what_is_found = check_for_deposit_rock(row, col)
    if what_is_found == 'rock':
        return 'broken'

    matrix[row][col] = 'E'
    return row, col


def check_for_deposit_rock(row, col):
    if matrix[row][col] == 'W':
        deposits["Water"] += 1
        print(f"Water deposit found at ({row}, {col})")
        return 'deposit'
    elif matrix[row][col] == 'M':
        deposits["Metal"] += 1
        print(f"Metal deposit found at ({row}, {col})")
        return 'deposit'
    elif matrix[row][col] == 'C':
        deposits["Concrete"] += 1
        print(f"Concrete deposit found at ({row}, {col})")
        return 'deposit'
    elif matrix[row][col] == 'R':
        print(f"Rover got broken at ({row}, {col})")
        return 'rock'


deposits = {"Water": 0, "Metal": 0, "Concrete": 0}

# finds the rover in the matrix
rover_row, rover_col = [(row, col) for col in range(6) for row in range(6) if matrix[row][col] == 'E'][0]

for command in commands:
    if command == 'up':
        movement = move_rover(rover_row-1, rover_col)
        if movement == 'broken':
            break
        else:
            rover_row, rover_col = movement
    elif command == 'down':
        movement = move_rover(rover_row + 1, rover_col)
        if movement == 'broken':
            break
        else:
            rover_row, rover_col = movement
    elif command == 'left':
        movement = move_rover(rover_row, rover_col - 1)
        if movement == 'broken':
            break
        else:
            rover_row, rover_col = movement
    elif command == 'right':
        movement = move_rover(rover_row, rover_col + 1)
        if movement == 'broken':
            break
        else:
            rover_row, rover_col = movement

if 0 in deposits.values():
    print("Area not suitable to start the colony.")
else:
    print("Area suitable to start the colony. ")
