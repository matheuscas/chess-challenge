"""
    This module holds functions and constants more related to the chess itself,
    such as chess pieces indexing and movements.
"""

import util

KING = 1
QUEEN = 2
BISHOP = 3
ROOK = 4
KNIGHT = 5
OCCUPIED = -1
PIECES = [KING, QUEEN, BISHOP, ROOK, KNIGHT]


def fill_board_w_king(board_index, board_copy, lines, cols):
    """It tries to put a KING into board in board_index provided.

    Keyword arguments:
    board_index -- Index where the piece could be put.
    board -- A copy of the board array to do not change the original with local modification.
    lines -- Number of board lines (integer)
    cols -- Number of board columns (integer)
    """
    col = util.get_col_by_index(board_index, cols)
    line = util.get_line_by_index(board_index, lines)

    local_board = board_copy[:]

    # mirror to right (if possible)
    if col < (cols - 1):
        if local_board[board_index + 1] in PIECES:
            return False
        local_board[board_index + 1] = OCCUPIED

    # mirror to left (if possible)
    if col > 0:
        if local_board[board_index - 1] in PIECES:
            return False
        local_board[board_index - 1] = OCCUPIED

    # mirror down (if possible)
    if line < lines:
        if local_board[board_index + cols] in PIECES:
            return False
        local_board[board_index + cols] = OCCUPIED

    # mirror up (if possible)
    if line > 1:
        if local_board[board_index - cols] in PIECES:
            return False
        local_board[board_index - cols] = OCCUPIED

    # Diagonals

    # upper left
    if col > 0 and line > 1:
        if local_board[board_index - cols - 1] in PIECES:
            return False
        local_board[board_index - cols - 1] = OCCUPIED

    # down left
    if col > 0 and line < lines:
        if local_board[board_index + cols - 1] in PIECES:
            return False
        local_board[board_index + cols - 1] = OCCUPIED

    # upper right
    if col < (cols - 1) and line > 1:
        if local_board[board_index - cols + 1] in PIECES:
            return False
        local_board[board_index - cols + 1] = OCCUPIED

    # down right
    if col < (cols - 1) and line < lines:
        if local_board[board_index + cols + 1] in PIECES:
            return False
        local_board[board_index + cols + 1] = OCCUPIED

    if board_copy[board_index] != 0:
        return False
    else:
        board_copy = local_board
        board_copy[board_index] = KING

    return board_copy


def fill_board_w_rook(board_index, board_copy, lines, cols):
    """It tries to put a ROOK into board in board_index provided.

    Keyword arguments:
    board_index -- Index where the piece could be put.
    board -- A copy of the board array to do not change the original with local modification.
    lines -- Number of board lines (integer)
    cols -- Number of board columns (integer)
    """
    col = util.get_col_by_index(board_index, cols)
    line = util.get_line_by_index(board_index, lines)

    local_board = board_copy[:]

    # mirror to right (if possible)
    if col < (cols - 1):
        spaces = (cols - 1) - col
        for i in range(1, spaces + 1):
            if local_board[board_index + i] in PIECES:
                return False
            local_board[board_index + i] = OCCUPIED

    # mirror to left (if possible)
    if col > 0:
        spaces = col
        for i in range(1, spaces + 1):
            if local_board[board_index - i] in PIECES:
                return False
            local_board[board_index - i] = OCCUPIED

    # mirror down (if possible)
    if line < lines:
        spaces = lines - line
        for i in range(1, spaces + 1):
            if local_board[board_index + (cols * i)] in PIECES:
                return False
            local_board[board_index + (cols * i)] = OCCUPIED

    # mirror up (if possible)
    if line > 1:
        spaces = line - 1
        for i in range(1, spaces + 1):
            if local_board[board_index - (cols * i)] in PIECES:
                return False
            local_board[board_index - (cols * i)] = OCCUPIED

    if board_copy[board_index] != 0:
        return False
    else:
        board_copy = local_board
        board_copy[board_index] = ROOK

    return board_copy


def fill_board_w_knight(board_index, board_copy, lines, cols):
    """It tries to put a KNIGHT into board in board_index provided.

    Keyword arguments:
    board_index -- Index where the piece could be put.
    board -- A copy of the board array to do not change the original with local modification.
    lines -- Number of board lines (integer)
    cols -- Number of board columns (integer)
    """
    col = util.get_col_by_index(board_index, cols)
    line = util.get_line_by_index(board_index, lines)

    local_board = board_copy[:]

    # first mov: left and up
    if line > 1 and col > 1:
        if local_board[board_index - 2 - cols] in PIECES:
            return False
        local_board[board_index - 2 - cols] = OCCUPIED

    # second mov: up and left
    if line > 2 and col > 0:
        if local_board[board_index - (cols * 2) - 1] in PIECES:
            return False
        local_board[board_index - (cols * 2) - 1] = OCCUPIED

    # third mov: up and right
    if line > 2 and col < (cols - 1):
        if local_board[board_index - (cols * 2) + 1] in PIECES:
            return False
        local_board[board_index - (cols * 2) + 1] = OCCUPIED

    # fourth mov: right and up
    if line > 1 and col < (cols - 2):
        if local_board[board_index + 2 - cols] in PIECES:
            return False
        local_board[board_index + 2 - cols] = OCCUPIED

    # fifth mov: right and down
    if line < lines and col < (cols - 2):
        if local_board[board_index + 2 + cols] in PIECES:
            return False
        local_board[board_index + 2 + cols] = OCCUPIED

    # sixth mov: down and right
    if line <= (lines - 2) and col < (cols - 1):
        if local_board[board_index + (cols * 2) + 1] in PIECES:
            return False
        local_board[board_index + (cols * 2) + 1] = OCCUPIED

    # seventh mov: down and left
    if line <= (lines - 2) and col > 0:
        if local_board[board_index + (cols * 2) - 1] in PIECES:
            return False
        local_board[board_index + (cols * 2) - 1] = OCCUPIED

    # eighth mov: left and down
    if line < lines and col > 1:
        if local_board[board_index - 2 + cols] in PIECES:
            return False
        local_board[board_index - 2 + cols] = OCCUPIED

    if board_copy[board_index] != 0:
        return False
    else:
        board_copy = local_board
        board_copy[board_index] = KNIGHT

    return board_copy


def fill_board_w_queen(board_index, board_copy, lines, cols):
    """It tries to put a QUEEN into board in board_index provided.

    Keyword arguments:
    board_index -- Index where the piece could be put.
    board -- A copy of the board array to do not change the original with local modification.
    lines -- Number of board lines (integer)
    cols -- Number of board columns (integer)
    """
    col = util.get_col_by_index(board_index, cols)
    line = util.get_line_by_index(board_index, lines)

    local_board = board_copy[:]

    # mirror to right (if possible) like rook
    if col < (cols - 1):
        spaces = (cols - 1) - col
        for i in range(1, spaces + 1):
            if local_board[board_index + i] in PIECES:
                return False
            local_board[board_index + i] = OCCUPIED

    # mirror to left (if possible)
    if col > 0:
        spaces = col
        for i in range(1, spaces + 1):
            if local_board[board_index - i] in PIECES:
                return False
            local_board[board_index - i] = OCCUPIED

    # mirror down (if possible) like rook
    if line < lines:
        spaces = lines - line
        for i in range(1, spaces + 1):
            if local_board[board_index + (cols * i)] in PIECES:
                return False
            local_board[board_index + (cols * i)] = OCCUPIED

    # mirror up (if possible) like rook
    if line > 1:
        spaces = line - 1
        for i in range(1, spaces + 1):
            if local_board[board_index - (cols * i)] in PIECES:
                return False
            local_board[board_index - (cols * i)] = OCCUPIED

    # Diagonals

    # # upper left
    if col > 0 and line > 1:
        steps = col if col <= (line - 1) else (line - 1)
        for step in range(1, steps + 1):
            if local_board[board_index - (step * cols) - step] in PIECES:
                return False
            local_board[board_index - (step * cols) - step] = OCCUPIED

    # # down left
    if col > 0 and line < lines:
        steps = col if col <= (lines - line) else (lines - line)
        for step in range(1, steps + 1):
            if local_board[board_index + (cols * step) - step] in PIECES:
                return False
            local_board[board_index + (cols * step) - step] = OCCUPIED

    # # upper right
    if col < (cols - 1) and line > 1:
        steps = (cols - 1 - col) if (cols - 1 - col) <= (line - 1) else (line - 1)
        for step in range(1, steps + 1):
            if local_board[board_index - (cols * step) + step] in PIECES:
                return False
            local_board[board_index - (cols * step) + step] = OCCUPIED

    # # down right
    if col < (cols - 1) and line < lines:
        steps = (cols - 1 - col) if (cols - 1 - col) <= (lines - line) else (lines - line)
        for step in range(1, steps + 1):
            if local_board[board_index + (cols * step) + step] in PIECES:
                return False
            local_board[board_index + (cols * step) + step] = OCCUPIED

    # put the queen itself
    if board_copy[board_index] != 0:
        return False
    else:
        board_copy = local_board
        board_copy[board_index] = QUEEN

    return board_copy


def fill_board_w_bishop(board_index, board_copy, lines, cols):
    """It tries to put a BISHOP into board in board_index provided.

    Keyword arguments:
    board_index -- Index where the piece could be put.
    board -- A copy of the board array to do not change the original with local modification.
    lines -- Number of board lines (integer)
    cols -- Number of board columns (integer)
    """
    col = util.get_col_by_index(board_index, cols)
    line = util.get_line_by_index(board_index, lines)

    local_board = board_copy[:]

    # # upper left
    if col > 0 and line > 1:
        steps = col if col <= (line - 1) else (line - 1)
        for step in range(1, steps + 1):
            if local_board[board_index - (step * cols) - step] in PIECES:
                return False
            local_board[board_index - (step * cols) - step] = OCCUPIED

    # # down left
    if col > 0 and line < lines:
        steps = col if col <= (lines - line) else (lines - line)
        for step in range(1, steps + 1):
            if local_board[board_index + (cols * step) - step] in PIECES:
                return False
            local_board[board_index + (cols * step) - step] = OCCUPIED

    # # upper right
    if col < (cols - 1) and line > 1:
        steps = (cols - 1 - col) if (cols - 1 - col) <= (line - 1) else (line - 1)
        for step in range(1, steps + 1):
            if local_board[board_index - (cols * step) + step] in PIECES:
                return False
            local_board[board_index - (cols * step) + step] = OCCUPIED

    # # down right
    if col < (cols - 1) and line < lines:
        steps = (cols - 1 - col) if (cols - 1 - col) <= (lines - line) else (lines - line)
        for step in range(1, steps + 1):
            if local_board[board_index + (cols * step) + step] in PIECES:
                return False
            local_board[board_index + (cols * step) + step] = OCCUPIED

    # put the queen itself
    if board_copy[board_index] != 0:
        return False
    else:
        board_copy = local_board
        board_copy[board_index] = BISHOP

    return board_copy
