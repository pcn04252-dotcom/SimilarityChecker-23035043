from length import LengthChecker


def test_same_length_returns_60():
    checker = LengthChecker()
    assert checker.score("ABCDE", "FGHIJ") == 60