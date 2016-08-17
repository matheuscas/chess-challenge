from chess import * 

def test_fill_board_w_queen_second_col_second_line():
    board = [0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0]

    expected_board = [OCCUPIED,OCCUPIED,OCCUPIED,0,
                        OCCUPIED,QUEEN,OCCUPIED,OCCUPIED,
                        OCCUPIED,OCCUPIED,OCCUPIED,0,
                        0,OCCUPIED,0,OCCUPIED]

    M = N = 4
    queen_position = 5 # second col and second line
    updated_board = fill_board_w_queen(QUEEN, queen_position, board, M, N)
    assert updated_board == expected_board

def test_fill_board_w_queen_third_col_third_line():
    M = N = 4
    board = [0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0]

    expected_board = [OCCUPIED,0,OCCUPIED,0,
                        0,OCCUPIED,OCCUPIED,OCCUPIED,
                        OCCUPIED,OCCUPIED,QUEEN,OCCUPIED,
                        0,OCCUPIED,OCCUPIED,OCCUPIED]

    queen_position = 10 # third col and third line
    updated_board = fill_board_w_queen(QUEEN, queen_position, board, M, N)
    assert updated_board == expected_board

def test_fill_board_w_queen_first_col_first_line():
    M = N = 4
    board = [0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0]

    expected_board = [QUEEN,OCCUPIED,OCCUPIED,OCCUPIED,
                        OCCUPIED,OCCUPIED,0,0,
                        OCCUPIED,0,OCCUPIED,0,
                        OCCUPIED,0,0,OCCUPIED]

    queen_position = 0 # first col and first line
    updated_board = fill_board_w_queen(QUEEN, queen_position, board, M, N)
    assert updated_board == expected_board

def test_fill_board_w_queen_last_col_last_line():
    M = N = 4
    board = [0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0]

    expected_board = [OCCUPIED,0,0,OCCUPIED,
                        0,OCCUPIED,0,OCCUPIED,
                        0,0,OCCUPIED,OCCUPIED,
                        OCCUPIED,OCCUPIED,OCCUPIED,QUEEN]

    queen_position = 15 # last col and last line
    updated_board = fill_board_w_queen(QUEEN, queen_position, board, M, N)
    assert updated_board == expected_board

def test_fill_board_w_bishop_second_col_second_line():
    board = [0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0]

    expected_board = [OCCUPIED,0,OCCUPIED,0,
                        0,BISHOP,0,0,
                        OCCUPIED,0,OCCUPIED,0,
                        0,0,0,OCCUPIED]

    M = N = 4
    bishop_position = 5 # second col and second line
    updated_board = fill_board_w_bishop(BISHOP, bishop_position, board, M, N)
    assert updated_board == expected_board

def test_fill_board_w_bishop_third_col_third_line():
    M = N = 4
    board = [0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0]

    expected_board = [OCCUPIED,0,0,0,
                        0,OCCUPIED,0,OCCUPIED,
                        0,0,BISHOP,0,
                        0,OCCUPIED,0,OCCUPIED]

    bishop_position = 10 # third col and third line
    updated_board = fill_board_w_bishop(BISHOP, bishop_position, board, M, N)
    assert updated_board == expected_board

def test_fill_board_w_bishop_first_col_first_line():
    M = N = 4
    board = [0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0]

    expected_board = [BISHOP,0,0,0,
                        0,OCCUPIED,0,0,
                        0,0,OCCUPIED,0,
                        0,0,0,OCCUPIED]

    bishop_position = 0 # first col and first line
    updated_board = fill_board_w_bishop(BISHOP, bishop_position, board, M, N)
    assert updated_board == expected_board

def test_fill_board_w_bishop_last_col_last_line():
    M = N = 4
    board = [0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0]

    expected_board = [OCCUPIED,0,0,0,
                        0,OCCUPIED,0,0,
                        0,0,OCCUPIED,0,
                        0,0,0,BISHOP]

    bishop_position = 15 # last col and last line
    updated_board = fill_board_w_bishop(BISHOP, bishop_position, board, M, N)
    assert updated_board == expected_board

def test_fill_board_w_rook_second_col_second_line():
    board = [0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0]

    expected_board = [0,OCCUPIED,0,0,
                    OCCUPIED,ROOK,OCCUPIED,OCCUPIED,
                    0,OCCUPIED,0,0,
                    0,OCCUPIED,0,0]

    M = N = 4
    position = 5 # second col and second line
    updated_board = fill_board_w_rook(ROOK, position, board, M, N)
    assert updated_board == expected_board

def test_fill_board_w_rook_third_col_third_line():
    board = [0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0]

    expected_board = [0,0,OCCUPIED,0,
                    0,0,OCCUPIED,0,
                    OCCUPIED,OCCUPIED,ROOK,OCCUPIED,
                    0,0,OCCUPIED,0]

    M = N = 4
    position = 10
    updated_board = fill_board_w_rook(ROOK, position, board, M, N)
    assert updated_board == expected_board

def test_fill_board_w_rook_last_col_last_line():
    board = [0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0]

    expected_board = [0,0,0,OCCUPIED,
                    0,0,0,OCCUPIED,
                    0,0,0,OCCUPIED,
                    OCCUPIED,OCCUPIED,OCCUPIED,ROOK]

    M = N = 4
    position = 15
    updated_board = fill_board_w_rook(ROOK, position, board, M, N)
    assert updated_board == expected_board

def test_fill_board_w_rook_first_col_first_line():
    board = [0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0]

    expected_board = [ROOK,OCCUPIED,OCCUPIED,OCCUPIED,
                    OCCUPIED,0,0,0,
                    OCCUPIED,0,0,0,
                    OCCUPIED,0,0,0]

    M = N = 4
    position = 0
    updated_board = fill_board_w_rook(ROOK, position, board, M, N)
    assert updated_board == expected_board

def test_fill_board_w_king_second_col_second_line():
    board = [0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0]

    expected_board = [OCCUPIED,OCCUPIED,OCCUPIED,0,
                    OCCUPIED,KING,OCCUPIED,0,
                    OCCUPIED,OCCUPIED,OCCUPIED,0,
                    0,0,0,0]

    M = N = 4
    position = 5 # second col and second line
    updated_board = fill_board_w_king(KING, position, board, M, N)
    assert updated_board == expected_board

def test_fill_board_w_king_third_col_third_line():
    board = [0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0]

    expected_board = [0,0,0,0,
                    0,OCCUPIED,OCCUPIED,OCCUPIED,
                    0,OCCUPIED,KING,OCCUPIED,
                    0,OCCUPIED,OCCUPIED,OCCUPIED]

    M = N = 4
    position = 10
    updated_board = fill_board_w_king(KING, position, board, M, N)
    assert updated_board == expected_board

def test_fill_board_w_king_first_col_first_line():
    board = [0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0]

    expected_board = [KING,OCCUPIED,0,0,
                    OCCUPIED,OCCUPIED,0,0,
                    0,0,0,0,
                    0,0,0,0]

    M = N = 4
    position = 0
    updated_board = fill_board_w_king(KING, position, board, M, N)
    assert updated_board == expected_board

def test_fill_board_w_king_last_col_last_line():
    board = [0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0]

    expected_board = [0,0,0,0,
                    0,0,0,0,
                    0,0,OCCUPIED,OCCUPIED,
                    0,0,OCCUPIED,KING]

    M = N = 4
    position = 15
    updated_board = fill_board_w_king(KING, position, board, M, N)
    assert updated_board == expected_board

def test_fill_board_w_knight_second_col_second_line():
    board = [0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0]

    expected_board = [0,0,0,OCCUPIED,
                        0,KNIGHT,0,0,
                        0,0,0,OCCUPIED,
                        OCCUPIED,0,OCCUPIED,0]

    M = N = 4
    position = 5 # second col and second line
    updated_board = fill_board_w_knight(KNIGHT, position, board, M, N)
    assert updated_board == expected_board

def test_fill_board_w_knight_third_col_third_line():
    board = [0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0]

    expected_board = [0,OCCUPIED,0,OCCUPIED,
                    OCCUPIED,0,0,0,
                    0,0,KNIGHT,0,
                    OCCUPIED,0,0,0]

    M = N = 4
    position = 10
    updated_board = fill_board_w_knight(KNIGHT, position, board, M, N)
    assert updated_board == expected_board

def test_fill_board_w_knight_first_col_first_line():
    board = [0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0]

    expected_board = [KNIGHT,0,0,0,
                        0,0,OCCUPIED,0,
                        0,OCCUPIED,0,0,
                        0,0,0,0]

    M = N = 4
    position = 0
    updated_board = fill_board_w_knight(KNIGHT, position, board, M, N)
    assert updated_board == expected_board

def test_fill_board_w_knight_last_col_last_line():
    board = [0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0]

    expected_board = [0,0,0,0,
                        0,0,OCCUPIED,0,
                        0,OCCUPIED,0,0,
                        0,0,0,KNIGHT]

    M = N = 4
    position = 15
    updated_board = fill_board_w_knight(KNIGHT, position, board, M, N)
    assert updated_board == expected_board