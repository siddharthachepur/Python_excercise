class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while True:
            sum = 0
            for i in str(num):
                sum += int(i)
            if len(str(sum)) == 1:
                break
            else:
                num = sum
        return sum
#        r = 0
#        while num:
#            r, num = r + num %10, num // 10
#        return r
