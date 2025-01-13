class Solution:
    def minimumLength(self, s: str) -> int:
        res = 0
        hmap = [0]*26  # Frequency array for 26 lowercase English letters

        # Count the frequency of each character in the string
        for i in s:
            hmap[ord(i)-97] += 1

        #  minimum length of the final string
        for i in hmap:
            if i != 0:
                if i % 2 == 0:
                    res += 2
                else:
                    res += 1

        return res