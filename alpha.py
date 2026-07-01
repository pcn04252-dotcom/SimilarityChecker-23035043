class AlphaChecker:
    def score(self, a: str, b: str) -> int:
        set1 = set(a)
        set2 = set(b)

        same = len(set1 & set2)
        total = len(set1 | set2)

        if total == 0:
            return 40

        return int(same / total * 40)