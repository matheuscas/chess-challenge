def get_col_by_index(index, N):
    """
    It calculates the chess board column based on array index representations
    """

    return index % N

def get_line_by_index(index, M):
    """
    It calculates the chess board line based on array index representations
    """

    if index < M:
        return 1
    elif index == M:
        return 2
    elif index >= (M - 1) * M:
        return M
    else:
        for l in range(2, M):
            if index >= (l - 1) * M and index < l * M:
                return l
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