# -*- coding: utf-8 -*-
import itertools

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
            if index > (l - 1) * M and index < l * M:
                return l
    return -1


def mirror_king(index, mirror, configuration, M, N):
    """
    Mirror King's position where it could attack. Returns false if there is a piece in that space.
    A king moves one space to every side, except diagonals.
    """
    col = get_col_by_index(index, N)
    line = get_line_by_index(index, M)

    # mirror to righ (if possible)
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

    # upper righ
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

    return True

M = 3 # lines
N = 3 # cols
BOARD = M * N

# pieces
KING = 1
QUEEN = 2
BISHOP = 3
ROOK = 4
KNIGHT = 5

test_1 = [KING, KING, ROOK]
initial_conf = test_1 + (BOARD - len(test_1)) * [0]
# all_configurations = set(itertools.permutations(initial_conf))
valid_configurations = []
all_configurations = [
    (1,0,1,0,0,0,0,4,0),
    (1,0,0,0,0,4,1,0,0),
    (0,0,1,4,0,0,0,0,1),
    (0,4,0,0,0,0,1,0,1)
]
for conf in all_configurations:
    if is_valid_configuration(list(conf), M, N):
        print conf
        valid_configurations.append(list(conf))
print len(valid_configurations)
