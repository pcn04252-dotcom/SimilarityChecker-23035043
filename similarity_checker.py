from length import LengthChecker
from alpha import AlphaChecker


class SimilarityChecker:
    def __init__(self):
        self.length_checker = LengthChecker()
        self.alpha_checker = AlphaChecker()

    def score(self, a: str, b: str) -> int:
        return (
                self.length_checker.score(a, b)
                + self.alpha_checker.score(a, b)
        )
