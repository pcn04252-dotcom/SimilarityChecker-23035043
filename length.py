MAX_SCORE = 60


class LengthChecker:
    def score(self, a: str, b: str) -> int:
        long_len = max(len(a), len(b))
        short_len = min(len(a), len(b))

        if long_len == short_len:
            return MAX_SCORE

        if long_len >= short_len * 2:
            return 0

        gap = long_len - short_len
        return int((1 - gap / short_len) * MAX_SCORE)