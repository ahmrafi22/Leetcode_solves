class Solution:
    def clearDigits(self, s: str) -> str:
        chars = list(s)
        marked = [False] * len(chars)
        
        for i in range(len(chars)):
            if chars[i].isdigit():
                for j in range(i-1, -1, -1):
                    if not marked[j] and not chars[j].isdigit():
                        marked[j] = True
                        break
        
        return ''.join(char for i, char in enumerate(chars) 
                       if not marked[i] and not char.isdigit())
