import util

KING = 1
QUEEN = 2
BISHOP = 3
ROOK = 4
KNIGHT = 5

OCCUPIED = -1

PIECES = [KING, QUEEN, BISHOP, ROOK, KNIGHT]

def fill_board_w_king(perm_piece, board_index, board_copy, M, N):
    col = util.get_col_by_index(board_index, N)
    line = util.get_line_by_index(board_index, M)

    local_board = board_copy[:]

    # mirror to right (if possible)
    if col < (N - 1):
        if local_board[board_index + 1] in PIECES:
            return False
        local_board[board_index + 1] = OCCUPIED

    # mirror to left (if possible)
    if col > 0:
        if local_board[board_index - 1] in PIECES:
            return False
        local_board[board_index - 1] = OCCUPIED

    # mirror down (if possible)
    if line < M:
        if local_board[board_index + N] in PIECES:
            return False
        local_board[board_index + N] = OCCUPIED

    # mirror up (if possible)
    if line > 1:
        if local_board[board_index - N] in PIECES:
            return False
        local_board[board_index - N] = OCCUPIED

    # Diagonals

    # upper left
    if col > 0 and line > 1:
        if local_board[board_index - N - 1] in PIECES:
            return False
        local_board[board_index - N - 1] = OCCUPIED

    # down left
    if col > 0 and line < M:
        if local_board[board_index + N - 1] in PIECES:
            return False
        local_board[board_index + N - 1] = OCCUPIED

    # upper right
    if col < (N - 1) and line > 1:
        if local_board[board_index - N + 1] in PIECES:
            return False
        local_board[board_index - N + 1] = OCCUPIED

    # down right
    if col < (N - 1) and line < M:
        if local_board[board_index + N + 1] in PIECES:
            return False
        local_board[board_index + N + 1] = OCCUPIED

    
    if board_copy[board_index] != 0:
        return False
    else:
        board_copy = local_board
        board_copy[board_index] = KING

    return board_copy


def fill_board_w_rook(perm_piece, board_index, board_copy, M, N):
    col = util.get_col_by_index(board_index, N)
    line = util.get_line_by_index(board_index, M)

    local_board = board_copy[:]

    # mirror to right (if possible)
    if col < (N - 1):
        spaces = (N - 1) - col
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
    if line < M:
        spaces = M - line
        for i in range(1, spaces + 1):
            if local_board[board_index + (N * i)] in PIECES:
                return False
            local_board[board_index + (N * i)] = OCCUPIED

    # mirror up (if possible)
    if line > 1:
        spaces = line - 1
        for i in range(1, spaces + 1):
            if local_board[board_index - (N * i)] in PIECES:
                return False
            local_board[board_index - (N * i)] = OCCUPIED

    if board_copy[board_index] != 0:
        return False
    else:
        board_copy = local_board
        board_copy[board_index] = ROOK

    return board_copy


def fill_board_w_knight(perm_piece, board_index, board_copy, M, N):
    
    col = util.get_col_by_index(board_index, N)
    line = util.get_line_by_index(board_index, M)

    local_board = board_copy[:]

    #first mov: left and up
    if line > 1 and col > 1:
        if local_board[board_index - 2 - N] in PIECES:
            return False
        local_board[board_index - 2 - N] = OCCUPIED

    #second mov: up and left
    if line > 2 and col > 0:
        if local_board[board_index - (N * 2) - 1] in PIECES:
            return False
        local_board[board_index - (N * 2) - 1] = OCCUPIED

    #third mov: up and right
    if line > 2 and col < (N - 1):
        if local_board[board_index - (N * 2) + 1] in PIECES:
            return False
        local_board[board_index - (N * 2) + 1] = OCCUPIED

    #fourth mov: right and up
    if line > 1 and col < (N - 2):
        if local_board[board_index + 2 - N] in PIECES:
            return False
        local_board[board_index + 2 - N] = OCCUPIED

    #fifth mov: right and down
    if line < M and col < (N - 2):
        if local_board[board_index + 2 + N] in PIECES:
            return False
        local_board[board_index + 2 + N] = OCCUPIED

    #sixth mov: down and right
    if line < (M - 2) and col < (N - 1):
        if local_board[board_index + (N * 2) + 1] in PIECES:
            return False
        local_board[board_index + (N * 2) + 1] = OCCUPIED

    #seventh mov: down and left
    if line < (M - 2) and col > 0:
        if local_board[board_index + (N * 2) - 1] in PIECES:
            return False
        local_board[board_index + (N * 2) - 1] = OCCUPIED

    #eighth mov: left and down
    if line < M and col > 1:
        if local_board[board_index - 2 + N] in PIECES:
            return False
        local_board[board_index - 2 + N] = OCCUPIED

    if board_copy[board_index] != 0:
        return False
    else:
        board_copy = local_board
        board_copy[board_index] = KNIGHT

    return board_copy

def fill_board_w_queen(perm_piece, board_index, board_copy, M, N):
    
    col = util.get_col_by_index(board_index, N)
    line = util.get_line_by_index(board_index, M)

    local_board = board_copy[:]

    # mirror to right (if possible) like rook
    if col < (N - 1):
        spaces = (N - 1) - col
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
    if line < M:
        spaces = M - line
        for i in range(1, spaces + 1):
            if local_board[board_index + (N * i)] in PIECES:
                return False
            local_board[board_index + (N * i)] = OCCUPIED

    # mirror up (if possible) like rook
    if line > 1:
        spaces = line - 1
        for i in range(1, spaces + 1):
            if local_board[board_index - (N * i)] in PIECES:
                return False
            local_board[board_index - (N * i)] = OCCUPIED

    # Diagonals

    # # upper left
    if col > 0 and line > 1:
        steps = col if col <= (line - 1) else (line - 1)
        for step in range(1, steps + 1):
            if local_board[board_index - (step * N) - step] in PIECES:
                return False
            local_board[board_index - (step * N) - step] = OCCUPIED

    # # down left
    if col > 0 and line < M:
        steps = col if col <= (M - line) else (M - line)
        for step in range(1, steps + 1):
            if local_board[board_index + (N * step) - step] in PIECES:
                return False
            local_board[board_index + (N * step) - step] = OCCUPIED

    # # upper right
    if col < (N - 1) and line > 1:
        steps = (N - 1 - col) if (N - 1 - col) <= (line - 1) else (line - 1)
        for step in range(1, steps + 1):
            if local_board[board_index - (N * step) + step] in PIECES:
                return False
            local_board[board_index - (N * step) + step] = OCCUPIED

    # # down right
    if col < (N - 1) and line < M:
        steps = (N - 1 - col) if (N - 1 - col) <= (M - line) else (M - line)
        for step in range(1, steps + 1):
            if local_board[board_index + (N * step) + step] in PIECES:
                return False
            local_board[board_index + (N * step) + step] = OCCUPIED

    
    # put the queen itself
    if board_copy[board_index] != 0:
        return False
    else:
        board_copy = local_board
        board_copy[board_index] = QUEEN

    return board_copy

def fill_board_w_bishop(perm_piece, board_index, board_copy, M, N):
    
    col = util.get_col_by_index(board_index, N)
    line = util.get_line_by_index(board_index, M)

    local_board = board_copy[:]
    
    # # upper left
    if col > 0 and line > 1:
        steps = col if col <= (line - 1) else (line - 1)
        for step in range(1, steps + 1):
            if local_board[board_index - (step * N) - step] in PIECES:
                return False
            local_board[board_index - (step * N) - step] = OCCUPIED

    # # down left
    if col > 0 and line < M:
        steps = col if col <= (M - line) else (M - line)
        for step in range(1, steps + 1):
            if local_board[board_index + (N * step) - step] in PIECES:
                return False
            local_board[board_index + (N * step) - step] = OCCUPIED

    # # upper right
    if col < (N - 1) and line > 1:
        steps = (N - 1 - col) if (N - 1 - col) <= (line - 1) else (line - 1)
        for step in range(1, steps + 1):
            if local_board[board_index - (N * step) + step] in PIECES:
                return False
            local_board[board_index - (N * step) + step] = OCCUPIED

    # # down right
    if col < (N - 1) and line < M:
        steps = (N - 1 - col) if (N - 1 - col) <= (M - line) else (M - line)
        for step in range(1, steps + 1):
            if local_board[board_index + (N * step) + step] in PIECES:
                return False
            local_board[board_index + (N * step) + step] = OCCUPIED

    
    # put the queen itself
    if board_copy[board_index] != 0:
        return False
    else:
        board_copy = local_board
        board_copy[board_index] = BISHOP

    return board_copy
