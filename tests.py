import naive

def test_is_valid_configuration_3X3_2K1R():
    all_configurations = [
        (1,0,1,0,0,0,0,4,0),
        (1,0,0,0,0,4,1,0,0),
        (0,0,1,4,0,0,0,0,1),
        (0,4,0,0,0,0,1,0,1)
    ]

    M = N = 3

    for conf in all_configurations:
        assert naive.is_valid_configuration(list(conf), M, N) == True

def test_configuration_3X3_2K1R():
    pieces = [naive.KING, naive.KING, naive.ROOK]
    M = N = 3
    valid_configurations = [
        [1,0,1,0,0,0,0,4,0],
        [1,0,0,0,0,4,1,0,0],
        [0,0,1,4,0,0,0,0,1],
        [0,4,0,0,0,0,1,0,1]
    ]
    valid_confs = naive.chess_challenge(pieces, M, N)
    assert len(valid_confs)
    for vc in valid_confs:
        assert (vc in valid_configurations) == True

    