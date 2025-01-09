class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return (sum(wrd[0:len(pref)]==pref for wrd in words)) 
        