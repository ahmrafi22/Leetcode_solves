class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        index = []
        for i in range(len(s1)):
            if s1[i] != s2[i] :
                index.append(i)
            if len(index) > 2:
                return False
        
        return  len(index) == 2 and s1[index[0]] == s2[index[1]] and  s1[index[1]] == s2[index[0]]