# -*- coding: utf-8 -*-
import itertools

# pieces
KING = 1
QUEEN = 2
BISHOP = 3
ROOK = 4
KNIGHT = 5

def get_col_by_index(index, N):
    return index % N

def get_line_by_index(index, M):
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


def mirror_king(index, mirror, configuration, M, N):
    """
    Mirror King's position where it could attack. Returns false if there is a piece in that space.
    A king moves one space to every side.
    """

    col = get_col_by_index(index, N)
    line = get_line_by_index(index, M)

    # mirror to right (if possible)
    if col < (N - 1):
        if configuration[index + 1] != 0:
            return False
        else:
            mirror[index + 1] = KING

    # mirror to left (if possible)
    if col > 0:
        if configuration[index - 1] != 0:
            return False
        else:
            mirror[index - 1] = KING

    # mirror down (if possible)
    if line < M:
        if configuration[index + 3] != 0:
            return False
        else:
            mirror[index + 3] = KING

    # mirror up (if possible)
    if line > 1:
        if configuration[index - 3] != 0:
            return False
        else:
            mirror[index - 3] = KING

    # Diagonals

    # upper left
    if col > 0 and line > 1:
        if configuration[index - 3 - 1] != 0:
            return False
        else:
            mirror[index - 3 - 1] = KING

    # down left
    if col > 0 and line < M:
        if configuration[index + 3 - 1] != 0:
            return False
        else:
            mirror[index + 3 - 1] = KING

    # upper right
    if col < (N - 1) and line > 1:
        if configuration[index - 3 + 1] != 0:
            return False
        else:
            mirror[index - 3 + 1] = KING

    # down right
    if col < (N - 1) and line < M:
        if configuration[index + 3 + 1] != 0:
            return False
        else:
            mirror[index + 3 + 1] = KING

    return True


def mirror_rook(index, mirror, configuration, M, N):
    """
    Mirror Rook's position where it could attack. Returns false if there is a piece in that space.
    A ROOK moves through intire line and column from its position
    """
    
    col = get_col_by_index(index, N)
    line = get_line_by_index(index, M)

    # mirror to right (if possible)
    if col < (N - 1):
        spaces = (N - 1) - col
        for i in range(1, spaces + 1):
            if configuration[index + i] != 0:
                return False
            else:
                mirror[index + i] = ROOK

    # mirror to left (if possible)
    if col > 0:
        spaces = col
        for i in range(1, spaces + 1):
            if configuration[index - i] != 0:
                return False
            else:
                mirror[index - i] = ROOK

    # mirror down (if possible)
    if line < M:
        spaces = M - line
        for i in range(1, spaces + 1):
            if configuration[index + (N * i)] != 0:
                return False
            else:
                mirror[index + (N * i)] = ROOK

    # mirror up (if possible)
    if line > 1:
        spaces = line - 1
        for i in range(1, spaces + 1):
            if configuration[index - (N * i)] != 0:
                return False
            else:
                mirror[index - (N * i)] = ROOK

    return True

def mirror_knight(index, mirror, configuration, M, N):
    """
    Mirror Knight's position where it could attack. Returns false if there is a piece in that space.
    A Knight moves in 'L' moves. 
    """

    col = get_col_by_index(index, N)
    line = get_line_by_index(index, M)

    #first mov: left and up
    if line > 1 and col > 1:
        if configuration[index - 2 - N] != 0:
            return False
        else:
            mirror[index - 2 - N] = KNIGHT

    #second mov: up and left
    if line > 2 and col > 0:
        if configuration[index - (N * 2) - 1] != 0:
            return False
        else:
            mirror[index - (N * 2) - 1] = KNIGHT

    #third mov: up and right
    if line > 2 and col < (N - 1):
        if configuration[index - (N * 2) + 1] != 0:
            return False
        else:
            mirror[index - (N * 2) + 1] = KNIGHT

    #fourth mov: right and up
    if line > 1 and col < (N - 2):
        if configuration[index + 2 - N] != 0:
            return False
        else:
            mirror[index + 2 - N] = KNIGHT

    #fifth mov: right and down
    if line < M and col < (N - 2):
        if configuration[index + 2 + N] != 0:
            return False
        else:
            mirror[index + 2 + N] = KNIGHT

    #sixth mov: down and right
    if line < (M - 2) and col < (N - 1):
        if configuration[index + (N * 2) + 1] != 0:
            return False
        else:
            mirror[index + (N * 2) + 1] = KNIGHT

    #seventh mov: down and left
    if line < (M - 2) and col > 0:
        if configuration[index + (N * 2) - 1] != 0:
            return False
        else:
            mirror[index + (N * 2) - 1] = KNIGHT

    #eighth mov: left and down
    if line < M and col > 1:
        if configuration[index - 2 + N] != 0:
            return False
        else:
            mirror[index - 2 + N] = KNIGHT

    return True


def is_valid_configuration(configuration, M, N):
    mirror = list(configuration)
    for index, piece in enumerate(configuration):
        if piece == 0:
            continue

        if piece == KING:
            valid_mirror = mirror_king(index, mirror, configuration, M, N)
            if not valid_mirror:
                return False
        elif piece == ROOK:
            valid_mirror = mirror_rook(index, mirror, configuration, M, N)
            if not valid_mirror:
                return False
        elif piece == KNIGHT:
            valid_mirror = mirror_knight(index, mirror, configuration, M, N)
            if not valid_mirror:
                return False

    return True


def chess_challenge(pieces, M, N):
    BOARD = M * N
    initial_conf = pieces + (BOARD - len(pieces)) * [0]
    all_configurations = set(itertools.permutations(initial_conf))
    valid_configurations = []
    for conf in all_configurations:
        if is_valid_configuration(list(conf), M, N):
            valid_configurations.append(list(conf))
    return valid_configurations
