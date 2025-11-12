class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow = set("qwertyuiop")
        secondRow = set("asdfghjkl")
        thirdRow = set("zxcvbnm")
        
        rows = [firstRow, secondRow, thirdRow]
        result = []
        
        for word in words:
            word_lower = word.lower()
            for row in rows:
                if word_lower[0] in row:
                    if all(char in row for char in word_lower):
                        result.append(word)
                    break
        
        return result
