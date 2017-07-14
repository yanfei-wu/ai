from collections import Counter
assignments = []

def assign_value(values, box, value):
    """
    Assigns a value to a given box. If it updates the board record it.
    Must use this function to update values dictionary for Pygame to work
    """

    # Only append actions that actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values


def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # Find all instances of naked twins
    twins = [(box1, box2) for box1 in boxes for box2 in peers[box1] \
                if len(values[box1]) == 2 and set(values[box1]) == set(values[box2])]

    # Eliminate the naked twins as possibilities for their peers
    for pair in twins:
        # all unique peers of the twins
        unique_peers = set(peers[pair[0]] & peers[pair[1]])
        # iterate over all peers and remove the twin values from their possibilities
        for peer in unique_peers:
            for val in values[peer]:
                if val in values[pair[0]]:
                    values = assign_value(values, peer, values[peer].replace(val, ''))
    return values



def cross(A, B):
    """Cross product of elements in A and elements in B."""
    return [s+t for s in A for t in B]

rows = 'ABCDEFGHI'
cols = '123456789'    
boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
col_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diag_units = [[rows[i]+cols[i] for i in range(len(rows))], [rows[i]+cols[::-1][i] for i in range(len(rows))]]

diag_flag = True # flag indicating if it is diagonal sudoku
if diag_flag:
    unitlist = row_units + col_units + square_units + diag_units
else:
    unitlist = row_units + col_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)


def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    chars = []
    digits = '123456789'
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == '.':
            chars.append(digits)
    assert len(grid) == 81
    return dict(zip(boxes, chars))
    

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width) + ('|' if c in '36' else '') for c in cols))
        if r in 'CF': 
            print(line)


def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    solved_boxes = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_boxes:
        digit_taken = values[box]
        # iterate over the peers and remove the digit already taken by solved boxes
        for peer in peers[box]:
            values = assign_value(values, peer, values[peer].replace(digit_taken, ''))           
    return values


def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    for unit in unitlist:
        for digit in '123456789':
            # list of box with the digit contained in possibilities
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values = assign_value(values, dplaces[0], digit) # assign digit to dplaces[0]
    return values


def reduce_puzzle(values):
    """
    Iterate eliminate() and only_choice(). If at some point, there is a box with no available values, return False.
    If the sudoku is solved, return the sudoku.
    If after an iteration of both functions, the sudoku remains the same, return the sudoku.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        # Use the Eliminate Strategy
        values = eliminate(values)
        # Use the Only Choice Strategy
        values = only_choice(values)
        # Use the Naked Twins Strategy
        values = naked_twins(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


def search(values):
    """Using depth-first search and propagation, try all possible values."""
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved
    # Choose one of the unfilled squares with the fewest possibilities
    min_posibilities, unsolved_box = min((len(values[box]), box) for box in boxes if len(values[box]) > 1)
    # Use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for value in values[unsolved_box]:
        new_sudoku = values.copy()
        new_sudoku = assign_value(new_sudoku, unsolved_box, value)
        attempt = search(new_sudoku)
        if attempt:
            return attempt


def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    # Convert grid into a dict of values
    values = grid_values(grid)
    # solve the puzzle
    values = search(values)
    return values

if __name__ == '__main__':
    diag_sudoku_grid = '9.1....8.8.5.7..4.2.4....6...7......5..............83.3..6......9................'
    #diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
