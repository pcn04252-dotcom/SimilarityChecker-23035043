from alpha import AlphaChecker


def test_same_alphabet_returns_40():
    checker = AlphaChecker()
    assert checker.score("ASD", "DSA") == 40


def test_no_common_alphabet_returns_0():
    checker = AlphaChecker()
    assert checker.score("A", "BB") == 0

