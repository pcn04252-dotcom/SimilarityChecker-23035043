from similarity_checker import SimilarityChecker


def test_same_string_returns_100():
    checker = SimilarityChecker()

    assert checker.score("ABCDE", "ABCDE") == 100