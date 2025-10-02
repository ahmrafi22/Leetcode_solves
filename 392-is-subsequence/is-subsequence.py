class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a = list(s)  
        for ch in t:
            if not a:        
                break
            if a[0] == ch:   
                a.pop(0)     
        
        return len(a) == 0
