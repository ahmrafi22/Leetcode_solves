class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        st_collection = {}
        for i in s:
            st_collection[i] = st_collection.get(i, 0 ) + 1

        st_collection2 = {}
        for i in t:
            st_collection2[i] = st_collection2.get(i, 0 ) + 1

        return st_collection == st_collection2
        

