class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        chars = list(set(s))

        good_count = s.count(chars[0])
        for i in chars:
            if s.count(i) != good_count:
                return False
        return True