class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        lcs = ""
        i, j = m, n
        while i > 0 and j > 0:
            if s1[i-1] == s2[j-1]:
                lcs = s1[i-1] + lcs
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        
        result = ""
        i = j = 0
        for char in lcs:
            while i < len(s1) and s1[i] != char:
                result += s1[i]
                i += 1
            
            while j < len(s2) and s2[j] != char:
                result += s2[j]
                j += 1
            
            result += char
            i += 1
            j += 1
        
        result += s1[i:] + s2[j:]
        
        return result