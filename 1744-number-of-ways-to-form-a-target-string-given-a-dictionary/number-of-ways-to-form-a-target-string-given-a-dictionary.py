class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        MOD = 10**9 + 7
        t = len(target)
        n = len(words[0])
        
        # If target is longer than source words, it's impossible
        if t > n:
            return 0
            
        # Count frequency of each character at each position in words
        # counts[i][c] represents count of character c at position i
        counts = [[0] * 26 for _ in range(n)]
        for word in words:
            for i, char in enumerate(word):
                counts[i][ord(char) - ord('a')] += 1
                
        # dp[i][j] represents number of ways to form target[t-i:] starting from position j
        # We need t+1 rows for lengths 0 to t, and n-t+1 columns for possible starting positions
        dp = [[0] * (n - t + 1) for _ in range(t + 1)]
        
        # Base case: empty string can be formed in 1 way
        for j in range(n - t + 1):
            dp[0][j] = 1
            
        # Fill dp table
        for i in range(1, t + 1):
            # Current target character we're trying to match
            target_char = target[t - i]
            target_char_idx = ord(target_char) - ord('a')
            
            # Try all possible starting positions from right to left
            for j in range(n - t, -1, -1):
                # Position in the source words where we're looking for current character
                char_pos = t - i + j
                
                # Ways to use current position = 
                # (previous state * count of current character at current position)
                dp[i][j] = (dp[i - 1][j] * counts[char_pos][target_char_idx]) % MOD
                
                # Add ways without using current position (if not at rightmost position)
                if j < n - t:
                    dp[i][j] = (dp[i][j] + dp[i][j + 1]) % MOD
        
        return dp[t][0]