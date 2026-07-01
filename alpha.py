class AlphaChecker:
    def score(self, a: str, b: str) -> int:
        set1 = set(a)
        set2 = set(b)

        if set1 == set2:
            return 40

        if set1.isdisjoint(set2):
            return 0

        return 40