class Solution(object):

    def HammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bin_x = bin(x)[2:]
        bin_y = bin(y)[2:]
        count = 0
        if len(bin_y) > len(bin_x):
            bin_x = '0' * (len(bin_y) - len(bin_x)) + bin_x
        else:
            bin_y = '0' * (len(bin_x) - len(bin_y)) + bin_y
        for i, c in enumerate(bin_x):
            if c != bin_y[i]:
                count += 1
        return count