class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        min_len = min(len(s) for s in strs)
        
        result = ""
        for i in range(min_len): 
            char = strs[0][i]
            
            for s in strs[1:]:
                if s[i] != char:
                    return result
            
            result += char
        
        return result