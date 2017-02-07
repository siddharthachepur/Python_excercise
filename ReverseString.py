class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # This method is by using slicing
        # return s[::-1]
        #################################

        # This method is without using slicing or reverse function
        n = len(s)
        for i in range(0, n):
            min = int(i)
            max = int(n-i)-1
            if min == max:
                break
            else:
                tmp = s[max]
                s[max] = s[min]
                s[min] = tmp
        return s
