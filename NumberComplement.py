class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(bin(num)[2:].replace('0', '@').replace('1', '0').replace('@', '1'), 2)