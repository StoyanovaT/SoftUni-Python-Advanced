def get_col_sum(row, col, length, play_field):
    column_sum = 0
    for i in range(length):
        if play_field[i][col] != 'B':
            column_sum += int(play_field[i][col])

    return column_sum


def is_inside(r, c, s):
    return 0 <= r < s and 0 <= c < s


size = 6
matrix = [[x for x in input().split()] for _ in range(size)]
points = 0

won_price_info = []
prizes_info_dict = {
    'Football': [100, 199],
    'Teddy Bear': [200, 299],
    'Lego Construction Set': [300],
}
for trow in range(3):
    hit_coord = input().strip('()').split(', ')
    hit_row = int(hit_coord[0])
    hit_col = int(hit_coord[1])

    if is_inside(hit_row, hit_col, size) and matrix[hit_row][hit_col] == 'B':
        points += get_col_sum(hit_row, hit_col, size, matrix)
        matrix[hit_row][hit_col] = 'H'
won_price = ''
if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
else:
    if points >= 300:
        won_price = 'Lego Construction Set'
    elif 200 <= points <= 299:
        won_price = 'Teddy Bear'
    else:
        won_price = 'Football'

    print(f"Good job! You scored {points} points, and you've won {won_price}.")

