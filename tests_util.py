import chess
import util

def test_has_valid_number_pieces_valid_configurations():
    
    original_permutation = [chess.KING, chess.KING, chess.ROOK]
    all_configurations = [
        [chess.KING,0,chess.KING,0,0,0,0,chess.ROOK,0],
        [chess.KING,0,0,0,0,chess.ROOK,chess.KING,0,0],
        [0,0,chess.KING,chess.ROOK,0,0,0,0,chess.KING],
        [0,chess.ROOK,0,0,0,0,chess.KING,0,chess.KING]
    ]

    for conf in all_configurations:
        assert util.has_valid_number_pieces(conf, original_permutation) == True

def test_has_valid_number_pieces_invalid_configurations():
    
    original_permutation = [chess.KING, chess.KING, chess.ROOK]
    all_configurations = [
        [chess.KING,chess.KING,0,0,0,0,0,chess.KING,0],
        [chess.KING,0,0,0,0,0,chess.KING,chess.KING,0],
        [0,chess.KING,chess.KING,0,0,0,0,0,chess.KING],
        [0,chess.KING,0,0,0,0,chess.KING,0,chess.KING]
    ]

    for conf in all_configurations:
        assert util.has_valid_number_pieces(conf, original_permutation) == False

def test_get_col_by_index():
    N = 3
    # [chess.KING,0,chess.KING,0,0,0,0,chess.ROOK,0]
    first_king_index = 0
    second_king_index = 2
    rook_index = 7
    expected_col_first_king = 0
    expected_col_second_king = 2
    expected_col_rook = 1

    assert util.get_col_by_index(first_king_index, N) == expected_col_first_king
    assert util.get_col_by_index(second_king_index, N) == expected_col_second_king
    assert util.get_col_by_index(rook_index, N) == expected_col_rook


def test_get_line_by_index():
    M = 3
    # [0,chess.KING,chess.KING,0,0,0,0,0,chess.KING]
    first_king_index = 1
    second_king_index = 2
    rook_index = 8
    expected_line_first_king = 1
    expected_line_second_king = 1
    expected_line_rook = 3

    assert util.get_line_by_index(first_king_index, M) == expected_line_first_king
    assert util.get_line_by_index(second_king_index, M) == expected_line_second_king
    assert util.get_line_by_index(rook_index, M) == expected_line_rook
 