MAX_SCORE = 40


class AlphaChecker:
    def score(self, a: str, b: str) -> int:
        set1 = set(a)
        set2 = set(b)

        same = len(set1 & set2)
        total = len(set1 | set2)

        if total == 0:
            return MAX_SCORE

        return int(same / total * MAX_SCORE)