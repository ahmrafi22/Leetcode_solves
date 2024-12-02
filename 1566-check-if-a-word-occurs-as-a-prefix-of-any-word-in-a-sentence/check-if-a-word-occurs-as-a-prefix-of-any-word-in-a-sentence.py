class Solution(object):

    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """

        listofwords = sentence.split(' ')  

        lenofwrd = len(searchWord)

        for (index, word) in enumerate(listofwords):
            if word[:lenofwrd] == searchWord:  
                return index + 1
        return -1
