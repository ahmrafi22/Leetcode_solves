class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        finalAns = ""
        start = 0  

        for space in spaces:
           finalAns += s[start:space] + " "
           start = space 


        finalAns += s[start:]

        return finalAns
        