from similarity_checker import SimilarityChecker


def test_same_string_returns_100():
    checker = SimilarityChecker()

    assert checker.score("ABCDE", "ABCDE") == 100


def test_completely_different_returns_0():
    checker = SimilarityChecker()

    assert checker.score("A", "BB") == 0

def test_partial_similarity():
    checker = SimilarityChecker()

    assert checker.score("AA", "AAE") == 50