class Solution(object):

    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        current = 0
        for num in nums:
            if num == 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 0
        return max(longest,current)