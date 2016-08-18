"""
    This module holds functions more related to the challenge,
    such as finding a valid piece position.
"""

import chess
import util


def __update_board(board, perm_piece, board_index, lines, cols):
    """Updates board, if possible, with the chess piece and attack range.

    Keyword arguments:
    board -- An array of integers that representes a board
    perm_piece -- A chess piece from a given permutation, such as a KING (1) or a QUEEN (2)
    board_index -- Index where the perm_piece could be put.
    lines -- Number of board lines (integer)
    cols -- Number of board columns (integer)
    """
    board_copy = board[:]
    if perm_piece == chess.KING:
        return chess.fill_board_w_king(
            board_index, board_copy, lines, cols)
    elif perm_piece == chess.ROOK:
        return chess.fill_board_w_rook(
            board_index, board_copy, lines, cols)
    elif perm_piece == chess.KNIGHT:
        return chess.fill_board_w_knight(
            board_index, board_copy, lines, cols)


def __find_valid_position_to(perm, board, original_perm, lines, cols):
    """Tries to find a valid position to all pieces for a given permutation into the board

    Keyword arguments:
    perm -- Abbreviation for permutation. A list of pieces to put on the board.
            Here is called 'permutation' (list of integers)
    board -- An array of integers that representes a board
    original_perm -- Abbreviation for original permutation.
                    This is the original list of pieces that the user pass in the begining
    lines -- Number of board lines (integer)
    cols -- Number of board columns (integer)
    """
    valid_configurations = []
    for perm_index in range(0, len(perm)):
        for board_index, board_piece in enumerate(board):
            if board_piece == 0:  # empty space
                updated_board = __update_board(
                    board, perm[perm_index], board_index, lines, cols)
                if not updated_board:
                    continue
                if util.has_valid_number_pieces(updated_board, original_perm):
                    valid_configurations.append(updated_board)
                valid_configurations = valid_configurations + \
                    __find_valid_position_to(perm[1:], updated_board, original_perm, lines, cols)
    return valid_configurations


def chess_challenge(permutation, lines, cols):
    """Main method of the challenge

    Keyword arguments:
    permutation -- The list of pieces to put on the board.
                    Here is called 'permutation' (list of integers)
    lines -- Number of board lines (integer)
    cols -- Number of board columns (integer)
    """
    length = lines * cols
    board = length * [0]
    valid_configurations = __find_valid_position_to(permutation, board, permutation, lines, cols)
    unique_configurations = []
    # filter unique
    for valid_config in valid_configurations:
        if valid_config not in unique_configurations:
            unique_configurations.append(valid_config)

    # change occupied spots to be black spots
    for unique_config in unique_configurations:
        for idx, i in enumerate(unique_config):
            if i == -1:
                unique_config[idx] = 0
    return unique_configurations
