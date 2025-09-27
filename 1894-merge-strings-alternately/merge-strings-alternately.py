class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1=len(word1)
        w2=len(word2)
        diff = w1 if w1 <  w2 else w2
        res= ""
        i=0
        j=0
        while i < diff:
            res+= word1[i]+word2[j]
            i+=1
            j+=1
        
        res+=word1[i:] + word2[j:]
        return res
