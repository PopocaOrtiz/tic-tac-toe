matriz = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]


def print_row(row):
    print('|', row[0],row[1],row[2],'|')


def print_matriz():
    print('---------')
    [print_row(row) for row in matriz]
    print('---------')


def get_col(index):
    return [row[index] for row in matriz]


def three_in_a_row(search, row):
    return row.count(search) == 3


def three_in_matriz(search):
    amount_of_threes = 0

    # threes in rows
    for row in matriz:
        if three_in_a_row(search,row):
            amount_of_threes += 1

    # threes in cols
    for col_number in range(3):
        if three_in_a_row(search, get_col(col_number)):
            amount_of_threes += 1

    # diagonals
    if matriz[0][0] == matriz[1][1] == matriz[2][2] == search:
        amount_of_threes += 1

    if matriz[0][2] == matriz[1][1] == matriz[2][0] == search:
        amount_of_threes += 1

    return amount_of_threes


def get_symbols_in_matrix(symbol):
    return [matriz[row][col] == symbol for row in range(3) for col in range(3)]


def check_result():

    x_threes_in_a_row = three_in_matriz('X')
    o_threes_in_a_row = three_in_matriz('O')

    if x_threes_in_a_row:
        print('X wins')
        return True
    elif o_threes_in_a_row:
        print('O wins')
        return True
    elif any(get_symbols_in_matrix(' ')):
        return
    else:
        print('Draw')
        return True


def is_valid_corrdinate(coordinate):
    return coordinate in ["1","2","3"]


def input_has_errors(input: str):

    x, y = input.split()

    if not (x.isdigit() and y.isdigit()):
        return 'You should enter numbers!'

    if not (is_valid_corrdinate(x) and is_valid_corrdinate(y)):
        return 'Coordinates should be from 1 to 3!'

    if not matriz[int(x)-1][int(y)-1] == ' ':
        return 'This cell is occupied! Choose another one!'

    return None


print_matriz()
next_symbol = 'X'

while True:

    print('Enter the coordinates:', end='')

    coordinates = input()

    input_error = input_has_errors(coordinates)

    if input_error:
        print(input_error)
        continue

    x, y = [int(n) - 1 for n in coordinates.split()]

    matriz[x][y] = next_symbol
    print_matriz()
    if check_result():
        break

    next_symbol = 'X' if next_symbol == 'O' else 'X'
