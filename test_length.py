from length import LengthChecker


def test_same_length_returns_60():
    checker = LengthChecker()
    assert checker.score("ABCDE", "FGHIJ") == 60


def test_more_than_twice_length_difference_returns_0():
    checker = LengthChecker()
    assert checker.score("A", "BB") == 0

