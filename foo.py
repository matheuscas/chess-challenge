from naive import *

#(1, 4, 1)
#(1, 1, 4)
#(4, 1, 1)
def fill_board_w_king(perm_piece, board_index, board_copy, M, N):
    col = get_col_by_index(board_index, N)
    line = get_line_by_index(board_index, M)

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
    col = get_col_by_index(board_index, N)
    line = get_line_by_index(board_index, M)

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
    
    col = get_col_by_index(board_index, N)
    line = get_line_by_index(board_index, M)

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



def update_board(board, perm_piece, board_index):
    board_copy = board[:]
    if perm_piece == KING:
        return fill_board_w_king(perm_piece, board_index, board_copy, M, N)
    elif perm_piece == ROOK:
        return fill_board_w_rook(perm_piece, board_index, board_copy, M, N)
    elif perm_piece == KNIGHT:
        return fill_board_w_knight(perm_piece, board_index, board_copy, M, N)

def is_valid_configuration(configuration, original_perm):
    pieces = set(original_perm)
    while len(pieces) > 0:
        piece = pieces.pop()
        if original_perm.count(piece) != configuration.count(piece):
            return False
    return True

def find_valid_position_to(perm, board, original_perm):
    valid_configurations = []
    for perm_index, perm_piece in enumerate(perm):
        for board_index, board_piece in enumerate(board):
            if board_piece == 0: # empty space
                updated_board = update_board(board, perm_piece, board_index)
                if not updated_board:
                    continue
                if is_valid_configuration(updated_board, original_perm):
                    valid_configurations.append(updated_board)
                valid_configurations = valid_configurations + find_valid_position_to(perm[1:], updated_board, original_perm)
    return valid_configurations

perm = [ROOK, ROOK, KNIGHT, KNIGHT, KNIGHT, KNIGHT]
M = N = 4
length = M * N
board = length * [0]
valid_configurations = find_valid_position_to(perm, board, perm)
unique_configurations = []
for vc in valid_configurations:
    if vc not in unique_configurations:
        unique_configurations.append(vc)

for uc in unique_configurations:
    print uc