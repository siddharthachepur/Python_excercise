class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # if you can pick the stones in a way that there are 4 stones left, then you can win the game
        return bool(n % 4 != 0)
