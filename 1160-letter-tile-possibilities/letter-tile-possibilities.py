class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq = {}
        for c in tiles:
            freq[c] = freq.get(c, 0) + 1
        
        def backtrack(curr_freq):
            total = 0
            for char in curr_freq:
                if curr_freq[char] > 0:
                    curr_freq[char] -= 1
                    total += 1 + backtrack(curr_freq)
                    curr_freq[char] += 1
            return total
            
        return backtrack(freq)