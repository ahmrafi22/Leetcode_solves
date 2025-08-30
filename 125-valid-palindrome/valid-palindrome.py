class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''
        for i in s:
            if (48 <= ord(i) <= 57) or (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122):
                string += i.lower()
        return string == string[::-1]

        