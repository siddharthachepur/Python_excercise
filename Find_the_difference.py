class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import collections
        return list(collections.Counter(t)-collections.Counter(s))[0]