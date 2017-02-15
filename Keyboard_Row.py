class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]

        """
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        res = []
        for i in words:
            for j in rows:
                if set(i.lower()).issubset(set(j)):
                    res.append(i)
        return res
