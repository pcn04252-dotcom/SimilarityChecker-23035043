from length import LengthChecker
from alpha import AlphaChecker


class SimilarityChecker:
    def __init__(
        self,
        length_checker=None,
        alpha_checker=None,
    ):
        self.length_checker = length_checker or LengthChecker()
        self.alpha_checker = alpha_checker or AlphaChecker()

    def score(self, a: str, b: str) -> int:
        return (
            self.length_checker.score(a, b)
            + self.alpha_checker.score(a, b)
        )