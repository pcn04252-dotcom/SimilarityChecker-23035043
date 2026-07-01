from alpha import AlphaChecker


def test_same_alphabet_returns_40():
    checker = AlphaChecker()
    assert checker.score("ASD", "DSA") == 40