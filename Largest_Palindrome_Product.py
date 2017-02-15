class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        upper_limit = 0
        max_product = 0
        for i in range(1, n+1):
            upper_limit *= 10
            upper_limit += 9
        lower_limit = 1 + upper_limit/10
        for i in range(upper_limit, lower_limit-1, -1):
            for j in range(i, lower_limit-1, -1):
                product = i*j
                if product < max_product:
                    break
                if str(product) == str(product)[::-1] and product > max_product:
                    max_product = product
                    # print max_product
        return max_product
        # return int(max_product%1337)
