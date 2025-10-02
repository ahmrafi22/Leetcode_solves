class Solution:
    def reverseWords(self, s: str) -> str:
        b=" ".join(s.split())
        a= b.split(" ")
        a.reverse()
        return " ".join(a)