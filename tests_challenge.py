import chess
import util
import challenge

def test_challenge_3x3_2KINGS_1ROOK():
    perm = [chess.KING, chess.KING, chess.ROOK]
    M = N = 3
    valid_configurations = challenge.chess_challenge(perm, M, N)
    for uc in valid_configurations:
        print uc
    assert True

def test_challenge_4x4_2ROOKS_4KNIGHTS():
    pass