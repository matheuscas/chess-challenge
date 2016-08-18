"""
    This module holds accessory functions that helps to accomplish the other tasks,
    such as calculates a piece column/line based on index and the number of
    columns or lines.
"""


def get_col_by_index(index, cols):
    """
    It calculates the chess board column based on array index representations
    """
    return index % cols


def get_line_by_index(index, lines):
    """
    It calculates the chess board line based on array index representations
    """
    if index < lines:
        return 1
    elif index == lines:
        return 2
    elif index >= (lines - 1) * lines:
        return lines
    else:
        for line in range(2, lines):
            if index >= (line - 1) * lines and index < line * lines:
                return line
    return -1


def has_valid_number_pieces(configuration, original_permutation):
    """
    Checks if a certain chess configuration has the valid number of pieces
    """
    pieces = set(original_permutation)
    while len(pieces) > 0:
        piece = pieces.pop()
        if original_permutation.count(piece) != configuration.count(piece):
            return False
    return True
