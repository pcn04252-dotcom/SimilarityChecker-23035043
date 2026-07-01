class LengthChecker:
    def score(self, a: str, b: str) -> int:
        long_len = max(len(a), len(b))
        short_len = min(len(a), len(b))

        if long_len >= short_len * 2:
            return 0

        return 60