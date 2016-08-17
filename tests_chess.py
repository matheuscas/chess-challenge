from chess import QUEEN, fill_board_w_queen, OCCUPIED

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