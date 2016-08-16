import chess
import util
import challenge

def test_challenge_3x3_2KINGS_1ROOK():
    perm = [chess.KING, chess.KING, chess.ROOK]
    M = N = 3
    expected_results =[
        [chess.KING, 0, chess.KING, 0, 0, 0, 0, chess.ROOK, 0],                                                                                                                                                               
        [chess.KING, 0, 0, 0, 0, chess.ROOK, chess.KING, 0, 0],                                                                                                                                                              
        [0, 0, chess.KING, chess.ROOK, 0, 0, 0, 0, chess.KING],                                                                                                                                                               
        [0, chess.ROOK, 0, 0, 0, 0, chess.KING, 0, chess.KING],   
    ]
    results = challenge.chess_challenge(perm, M, N)
    for uc in results:
        assert (uc in expected_results) == True

def test_challenge_4x4_2ROOKS_4KNIGHTS():
    pass