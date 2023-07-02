
  
lst = list('_________')


def print_matrix():
    print('---------')
    print('| {0} {1} {2} |'.format(lst[0], lst[1], lst[2]))
    print('| {0} {1} {2} |'.format(lst[3], lst[4], lst[5]))
    print('| {0} {1} {2} |'.format(lst[6], lst[7], lst[8]))
    print('---------')


def is_win(i, j, k):
    return lst[i] if lst[i] == lst[j] == lst[k] else ''


def count(sym):
    return len([i for i in lst if i == sym])


print_matrix()
current_sym = 'X'
while True:
    try:
        x_str, y_str = input('Enter the coordinates:').split(' ')

        x = int(x_str)
        y = int(y_str)
        if x in (1, 2, 3) and y in (1, 2, 3):
            ind = x - 3 * y + 8
            if lst[ind] in ('X', 'O'):
                print('This cell is occupied! Choose another one!')
            else:
                lst[ind] = current_sym
                current_sym = 'X' if current_sym == 'O' else 'O'
                print_matrix()
                win = is_win(0, 1, 2) + is_win(3, 4, 5) + is_win(6, 7, 8) + is_win(2, 4, 6) \
                    + is_win(0, 3, 6) + is_win(1, 4, 7) + is_win(2, 5, 8) + is_win(0, 4, 8)
                if win == 'O':
                    print('O wins')
                    break
                elif win == 'X':
                    print('X wins')
                    break
                else:
                    if count('_') == 0:
                        print('Draw')
                        break
        else:
            print('Coordinates should be from 1 to 3!')
    except TypeError:
        print('You should enter numbers!')
--------------------------------------------------------------------------------
def has_won(cells, char):
    return any(filter(lambda row: len(row) == 3, [
        [cell for cell in cells[0:3] if cell == char],
        [cell for cell in cells[3:6] if cell == char],
        [cell for cell in cells[6:9] if cell == char],

        [cell for cell in cells[0:9:3] if cell == char],
        [cell for cell in cells[1:9:3] if cell == char],
        [cell for cell in cells[2:9:3] if cell == char],

        [cell for cell in cells[0:9:4] if cell == char],
        [cell for cell in cells[2:7:2] if cell == char],
    ]))
    
--------------------------------------------------------------------------------
cells_list = list("_________")


def print_cells():
    print("---------")
    print("|", cells_list[0], cells_list[1], cells_list[2], "|")
    print("|", cells_list[3], cells_list[4], cells_list[5], "|")
    print("|", cells_list[6], cells_list[7], cells_list[8], "|")
    print("---------")


def take_coordinates():
    crs = input("Enter the coordinates:").split()
    while len(crs) != 2 or not crs[0].isdecimal() or not crs[1].isdecimal():
        print("You should enter numbers!")
        crs = input("Enter the coordinates:").split()
    crs = [int(x) for x in crs]
    return crs


def place_coordinates(crs, move):
    if crs[0] not in range(1, 4) or crs[1] not in range(1, 4):
        print("Coordinates should be from 1 to 3!")
        return False
    if crs[0] == 1:
        cells_column = (0, 3, 6)
    elif crs[0] == 2:
        cells_column = (1, 4, 7)
    else:
        cells_column = (2, 5, 8)
    if crs[1] == 1:
        cells_row = (6, 7, 8)
    elif crs[1] == 2:
        cells_row = (3, 4, 5)
    else:
        cells_row = (0, 1, 2)
    cell = 0
    for i in range(9):
        if i in cells_row and i in cells_column:
            cell = i
            break
    if cells_list[cell] != "_":
        print("This cell is occupied! Choose another one!")
        return False
    else:
        cells_list[cell] = move
        return True


def check_results():
    cells = "".join(cells_list)
    straights = [cells[:3], cells[3:6], cells[6:], cells[0:7:3], cells[1:8:3], cells[2:9:3], cells[0:9:4], cells[2:7:2]]
    if abs(len([x for x in cells_list if x == "X"]) - len([x for x in cells_list if x == "O"])) > 1:
        print("Impossible")
    elif "XXX" in straights and "OOO" in straights:
        print("Impossible")
    elif "XXX" in straights:
        print("X wins")
    elif "OOO" in straights:
        print("O wins")
    elif len([x for x in cells_list if x == "_"]) > 0:
        # print("Game not finished")
        return False
    else:
        print("Draw")
    return True


print_cells()
is_finished = False
who_moves = "X"
while not is_finished:
    is_placed = False
    while not is_placed:
        coordinates = take_coordinates()
        is_placed = place_coordinates(coordinates, who_moves)
    if who_moves == "X":
        who_moves = "O"
    else:
        who_moves = "X"
    print_cells()
    is_finished = check_results()
 ---------------------------------------------------------------------------------------
 # All possible winner positions
WINNER_POSITIONS = ({0, 1, 2}, {3, 4, 5}, {6, 7, 8},
                    {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
                    {0, 4, 8}, {2, 4, 6})

CHAR_X = "X"
CHAR_O = "O"


def convert_coordinates(coord_x, coord_y):
    """Converts coordinate from user input to position in the field list"""

    return (coord_x - 1) + (3 * (3 - coord_y))


def cell_occupied(coord_x, coord_y):
    """Checks that a cell with the entered coordinates is occupied"""

    return not field[convert_coordinates(coord_x, coord_y)] == " "


def user_input_correct(checked_input):
    global user_x
    global user_y

    try:
        user_x, user_y = [int(x) for x in checked_input.split()]
    except ValueError:
        print("You should enter numbers!")
        return False

    if user_x > 3 or user_y > 3 or user_x < 1 or user_y < 1:
        print("Coordinates should be from 1 to 3!")
        return False
    elif cell_occupied(user_x, user_y):
        print("This cell is occupied! Choose another one!")
        return False

    # All seems OK
    return True


def is_winner(char):
    # Create a set with the current position for the char
    current_pos = {i for i in range(len(field)) if field[i] == char}

    # Check that the current position includes a winner position
    for winner_pos in WINNER_POSITIONS:
        if current_pos.issuperset(winner_pos):
            return True

    # No winner position
    return False


def check_winner():
    global winner
    if is_winner(CHAR_X):
        winner = CHAR_X
    elif is_winner(CHAR_O):
        winner = CHAR_O


def no_more_turns():
    return field.count(" ") == 0


def game_finished():
    return no_more_turns() or winner is not None


def check_state():
    if winner is not None:
        print(f"{winner} wins")
    elif no_more_turns():
        print("Draw")


def update_field(coord_x, coord_y, char):
    field[convert_coordinates(coord_x, coord_y)] = char


def print_field():
    """Draw the game field in console"""

    print(9 * "-")
    for row in range(3):
        print("|", " ".join(field[row * 3: 3 + row * 3]), "|")
    print(9 * "-")


# Main program

# Initial parameters
winner = None
current_turn = CHAR_X  # X starts first
user_x = 0
user_y = 0

# Initiate blank 3x3 field
field = list(9 * " ")
print_field()

# Main game loop
while not game_finished():

    user_input = input("Enter the coordinates:")

    if user_input_correct(user_input):
        update_field(user_x, user_y, current_turn)
        current_turn = CHAR_X if current_turn == CHAR_O else CHAR_O
        print_field()
        check_winner()
        check_state()