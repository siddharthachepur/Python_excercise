class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # The complement strategy is to flip the bits of its binary representation.
        return int(bin(num)[2:].replace('0', '@').replace('1', '0').replace('@', '1'), 2)