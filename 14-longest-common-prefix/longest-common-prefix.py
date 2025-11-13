class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        result = ""

        for i in range(len(strs[0])):
            char = strs[0][i]

            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return result
            
            result +=char
        
        return result 