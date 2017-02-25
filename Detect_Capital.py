class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word == word.upper() or word == word.lower():
            return True
        elif word[0] == word[0].upper() and word[1:len(word)+1] == word[1:len(word)+1].lower():
            return True
        else:
            return False
