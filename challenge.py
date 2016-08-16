import chess
import util

def __update_board(board, perm_piece, board_index, M, N):
    board_copy = board[:]
    if perm_piece == chess.KING:
        return chess.fill_board_w_king(perm_piece, board_index, board_copy, M, N)
    elif perm_piece == chess.ROOK:
        return chess.fill_board_w_rook(perm_piece, board_index, board_copy, M, N)
    elif perm_piece == chess.KNIGHT:
        return chess.fill_board_w_knight(perm_piece, board_index, board_copy, M, N)

def __find_valid_position_to(perm, board, original_perm, M, N):
    valid_configurations = []
    for perm_index, perm_piece in enumerate(perm):
        for board_index, board_piece in enumerate(board):
            if board_piece == 0: # empty space
                updated_board = __update_board(board, perm_piece, board_index, M, N)
                if not updated_board:
                    continue
                if util.has_valid_number_pieces(updated_board, original_perm):
                    valid_configurations.append(updated_board)
                valid_configurations = valid_configurations + __find_valid_position_to(perm[1:], updated_board, original_perm, M, N)
    return valid_configurations

def chess_challenge(perm, M, N):
    length = M * N
    board = length * [0]
    valid_configurations = __find_valid_position_to(perm, board, perm, M, N)
    unique_configurations = []
    #filter unique
    for vc in valid_configurations:
        if vc not in unique_configurations:
            unique_configurations.append(vc)
    
    # change occupied spots to be black spots
    for uc in unique_configurations:
        for idx, i in enumerate(uc):
            if i == -1:
                uc[idx] = 0
    return unique_configurations